"""
Restaurant POS System - Android App
مطعم الأصيل - نظام الكاشير للأندرويد
Designed by: A7MED ASHRAF
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.metrics import dp
import sqlite3
import os
from datetime import datetime
import webbrowser

# Database path for Android
DB_PATH = os.path.join(os.environ.get('ANDROID_STORAGE', os.path.expanduser('~')), 
                       'restaurant_pos.db')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL,
        active INTEGER DEFAULT 1
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        order_date TEXT,
        table_num TEXT,
        subtotal REAL,
        tax REAL,
        total REAL,
        items TEXT
    )""")

    c.execute("SELECT COUNT(*) FROM products")
    if c.fetchone()[0] == 0:
        sample = [
            ("كشري", 45, "main"), ("فول مدمس", 20, "main"), ("طعمية", 15, "main"),
            ("شاورما لحمة", 85, "main"), ("شاورما فراخ", 75, "main"),
            ("بطاطس مقلية", 25, "appetizer"), ("حمص", 20, "appetizer"),
            ("بابا غنوج", 22, "appetizer"), ("تبولة", 30, "appetizer"),
            ("بيبسي", 15, "drink"), ("عصير مانجو", 25, "drink"),
            ("شاي", 10, "drink"), ("قهوة تركي", 18, "drink"),
            ("أم علي", 35, "dessert"), ("بسبوسة", 20, "dessert"),
            ("كنافة", 40, "dessert"), ("محلبية", 18, "dessert"),
            ("كفتة مشوية", 120, "main"), ("فتة", 55, "main"),
            ("مولتن كيك", 45, "dessert"),
        ]
        c.executemany("INSERT INTO products (name, price, category) VALUES (?,?,?)", sample)

    conn.commit()
    conn.close()

class ProductCard(Button):
    def __init__(self, product_id, name, price, category, **kwargs):
        super().__init__(**kwargs)
        self.product_id = product_id
        self.text = f"{name}\n{price:.0f} ج.م"
        self.font_size = '14sp'
        self.halign = 'center'
        self.valign = 'middle'
        self.size_hint_y = None
        self.height = dp(80)
        self.background_normal = ''

        colors = {
            'main': (0.906, 0.298, 0.235, 1),      # #e74c3c
            'appetizer': (0.953, 0.612, 0.071, 1),  # #f39c12
            'drink': (0.204, 0.596, 0.859, 1),      # #3498db
            'dessert': (0.608, 0.349, 0.714, 1),    # #9b59b6
        }
        self.background_color = colors.get(category, (0.8, 0.8, 0.8, 1))

class CartItem(BoxLayout):
    def __init__(self, item_data, remove_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = dp(40)
        self.padding = [dp(5), dp(2)]
        self.item_data = item_data

        self.add_widget(Label(text=item_data['name'], size_hint_x=0.4, font_size='13sp', 
                             color=(0.1, 0.1, 0.1, 1), halign='right'))
        self.add_widget(Label(text=f"x{item_data['qty']}", size_hint_x=0.15, font_size='13sp',
                             color=(0.4, 0.4, 0.4, 1)))
        self.add_widget(Label(text=f"{item_data['price']*item_data['qty']:.0f}", size_hint_x=0.25, 
                             font_size='13sp', color=(0.906, 0.298, 0.235, 1)))

        btn = Button(text='×', size_hint_x=0.2, font_size='16sp', 
                    background_color=(0.8, 0.2, 0.2, 1), background_normal='')
        btn.bind(on_press=lambda x: remove_callback(item_data['id']))
        self.add_widget(btn)

class RestaurantPOSApp(App):
    def build(self):
        Window.clearcolor = (0.96, 0.96, 0.96, 1)
        init_db()
        self.cart = []
        self.current_category = 'all'
        self.tax_rate = 0.14
        self.categories = {
            'all': 'الكل',
            'main': 'أطباق رئيسية',
            'appetizer': 'مقبلات',
            'drink': 'مشروبات',
            'dessert': 'حلويات'
        }

        # Main layout
        main = BoxLayout(orientation='vertical')

        # Header
        header = BoxLayout(size_hint_y=None, height=dp(50), padding=[dp(10), dp(5)])
        header.add_widget(Label(text='🍽️ مطعم الأصيل', font_size='18sp', 
                               color=(1, 1, 1, 1), bold=True, halign='right'))
        header.add_widget(Label(text=datetime.now().strftime('%Y-%m-%d'), font_size='12sp',
                               color=(0.8, 0.8, 0.8, 1)))
        with header.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(0.102, 0.102, 0.18, 1)
            self.header_rect = Rectangle(pos=header.pos, size=header.size)
        header.bind(pos=self._update_header_rect, size=self._update_header_rect)
        main.add_widget(header)

        # Content
        content = BoxLayout()

        # Left: Menu
        menu_panel = BoxLayout(orientation='vertical', size_hint_x=0.6)

        # Category buttons
        cat_box = BoxLayout(size_hint_y=None, height=dp(45), padding=[dp(5), dp(3)])
        self.cat_buttons = {}
        for key, label in self.categories.items():
            btn = Button(text=label, font_size='11sp', background_normal='')
            if key == 'all':
                btn.background_color = (0.906, 0.298, 0.235, 1)
            else:
                btn.background_color = (0.9, 0.9, 0.9, 1)
            btn.bind(on_press=lambda x, k=key: self.filter_category(k))
            cat_box.add_widget(btn)
            self.cat_buttons[key] = btn
        menu_panel.add_widget(cat_box)

        # Products grid
        scroll = ScrollView()
        self.products_grid = GridLayout(cols=2, spacing=dp(8), padding=dp(8), size_hint_y=None)
        self.products_grid.bind(minimum_height=self.products_grid.setter('height'))
        scroll.add_widget(self.products_grid)
        menu_panel.add_widget(scroll)

        content.add_widget(menu_panel)

        # Right: Cart
        cart_panel = BoxLayout(orientation='vertical', size_hint_x=0.4, 
                              padding=[dp(5), dp(5)])

        # Table number
        table_box = BoxLayout(size_hint_y=None, height=dp(40))
        table_box.add_widget(Label(text='الطاولة:', font_size='13sp', size_hint_x=0.4))
        self.table_input = TextInput(text='1', multiline=False, font_size='14sp',
                                    halign='center', input_filter='int', size_hint_x=0.6)
        table_box.add_widget(self.table_input)
        cart_panel.add_widget(table_box)

        cart_panel.add_widget(Label(text='🧾 الطلب الحالي', font_size='16sp', 
                                   color=(0.102, 0.102, 0.18, 1), size_hint_y=None, height=dp(35)))

        # Cart items
        cart_scroll = ScrollView()
        self.cart_layout = BoxLayout(orientation='vertical', size_hint_y=None, spacing=dp(2))
        self.cart_layout.bind(minimum_height=self.cart_layout.setter('height'))
        cart_scroll.add_widget(self.cart_layout)
        cart_panel.add_widget(cart_scroll)

        # Totals
        self.totals_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(100),
                                   padding=[dp(5), dp(5)])
        self.lbl_subtotal = Label(text='المجموع: 0.00 ج.م', font_size='13sp', 
                                 color=(0.3, 0.3, 0.3, 1), halign='right')
        self.lbl_tax = Label(text='الضريبة (14%): 0.00 ج.م', font_size='13sp',
                            color=(0.3, 0.3, 0.3, 1), halign='right')
        self.lbl_total = Label(text='الإجمالي: 0.00 ج.م', font_size='16sp', bold=True,
                              color=(0.906, 0.298, 0.235, 1), halign='right')
        self.totals_box.add_widget(self.lbl_subtotal)
        self.totals_box.add_widget(self.lbl_tax)
        self.totals_box.add_widget(self.lbl_total)
        cart_panel.add_widget(self.totals_box)

        # Buttons
        btn_box = BoxLayout(orientation='vertical', size_hint_y=None, height=dp(140), spacing=dp(5))
        btn_box.add_widget(Button(text='🖨️ طباعة الفاتورة', font_size='14sp',
                                 background_color=(0.102, 0.102, 0.18, 1), background_normal='',
                                 on_press=self.print_receipt))
        btn_box.add_widget(Button(text='💾 حفظ الطلب', font_size='14sp',
                                 background_color=(0.153, 0.682, 0.376, 1), background_normal='',
                                 on_press=self.save_order))
        btn_box.add_widget(Button(text='🗑️ إلغاء', font_size='14sp',
                                 background_color=(0.584, 0.647, 0.65, 1), background_normal='',
                                 on_press=self.clear_cart))
        cart_panel.add_widget(btn_box)

        # Designer Credit
        credit = Button(text='Designed by A7MED ASHRAF\n📞 01080343968', font_size='11sp',
                       background_color=(0.102, 0.102, 0.18, 1), background_normal='',
                       color=(0.945, 0.769, 0.059, 1), size_hint_y=None, height=dp(50),
                       halign='center')
        credit.bind(on_press=lambda x: webbrowser.open('https://a7medashraftarekh-cpu.github.io/A7MED-ASHRAF/'))
        cart_panel.add_widget(credit)

        content.add_widget(cart_panel)
        main.add_widget(content)

        self.load_products()
        return main

    def _update_header_rect(self, instance, value):
        self.header_rect.pos = instance.pos
        self.header_rect.size = instance.size

    def load_products(self):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        if self.current_category == 'all':
            c.execute("SELECT id, name, price, category FROM products WHERE active=1 ORDER BY category, name")
        else:
            c.execute("SELECT id, name, price, category FROM products WHERE category=? AND active=1 ORDER BY name",
                     (self.current_category,))
        products = c.fetchall()
        conn.close()

        self.products_grid.clear_widgets()
        for pid, name, price, cat in products:
            card = ProductCard(pid, name, price, cat)
            card.bind(on_press=lambda x, p=pid: self.add_to_cart(p))
            self.products_grid.add_widget(card)

    def filter_category(self, cat):
        self.current_category = cat
        for key, btn in self.cat_buttons.items():
            if key == cat:
                btn.background_color = (0.906, 0.298, 0.235, 1)
            else:
                btn.background_color = (0.9, 0.9, 0.9, 1)
        self.load_products()

    def add_to_cart(self, product_id):
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("SELECT id, name, price FROM products WHERE id=?", (product_id,))
        row = c.fetchone()
        conn.close()

        if not row:
            return

        pid, name, price = row
        for item in self.cart:
            if item['id'] == pid:
                item['qty'] += 1
                self.refresh_cart()
                return

        self.cart.append({'id': pid, 'name': name, 'price': price, 'qty': 1})
        self.refresh_cart()

    def remove_from_cart(self, product_id):
        for i, item in enumerate(self.cart):
            if item['id'] == product_id:
                if item['qty'] > 1:
                    item['qty'] -= 1
                else:
                    self.cart.pop(i)
                break
        self.refresh_cart()

    def refresh_cart(self):
        self.cart_layout.clear_widgets()

        subtotal = 0
        for item in self.cart:
            total = item['price'] * item['qty']
            subtotal += total
            self.cart_layout.add_widget(CartItem(item, self.remove_from_cart))

        tax = subtotal * self.tax_rate
        grand = subtotal + tax

        self.lbl_subtotal.text = f'المجموع: {subtotal:.2f} ج.م'
        self.lbl_tax.text = f'الضريبة (14%): {tax:.2f} ج.م'
        self.lbl_total.text = f'الإجمالي: {grand:.2f} ج.م'

    def clear_cart(self, *args):
        self.cart = []
        self.refresh_cart()

    def save_order(self, *args):
        if not self.cart:
            self.show_popup('تنبيه', 'السلة فارغة!')
            return

        subtotal = sum(i['price'] * i['qty'] for i in self.cart)
        tax = subtotal * self.tax_rate
        total = subtotal + tax
        items_str = "; ".join([f"{i['name']}x{i['qty']}" for i in self.cart])

        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("""INSERT INTO orders (order_date, table_num, subtotal, tax, total, items)
                     VALUES (?,?,?,?,?,?)""",
                  (datetime.now().isoformat(), self.table_input.text, subtotal, tax, total, items_str))
        conn.commit()
        conn.close()

        self.show_popup('تم', f'تم حفظ الطلب بنجاح!\nرقم الطاولة: {self.table_input.text}')
        self.clear_cart()

    def print_receipt(self, *args):
        if not self.cart:
            self.show_popup('تنبيه', 'السلة فارغة!')
            return

        subtotal = sum(i['price'] * i['qty'] for i in self.cart)
        tax = subtotal * self.tax_rate
        total = subtotal + tax

        receipt = f"""
{'='*35}
        مطعم الأصيل
   فاتورة ضريبية مبسطة
{'='*35}
التاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M')}
الطاولة: {self.table_input.text}
{'-'*35}
"""
        for item in self.cart:
            line_total = item['price'] * item['qty']
            receipt += f"{item['name']} x{item['qty']} = {line_total:.2f} ج.م\n"

        receipt += f"""
{'-'*35}
المجموع: {subtotal:.2f} ج.م
الضريبة: {tax:.2f} ج.م
{'='*35}
الإجمالي: {total:.2f} ج.م
{'='*35}
شكراً لزيارتكم!

Designed by A7MED ASHRAF
📞 01080343968
"""

        self.show_popup('فاتورة', receipt)
        self.clear_cart()

    def show_popup(self, title, message):
        box = BoxLayout(orientation='vertical', padding=dp(10))
        box.add_widget(Label(text=message, font_size='14sp', halign='center'))
        btn = Button(text='إغلاق', size_hint_y=None, height=dp(40),
                    background_color=(0.906, 0.298, 0.235, 1), background_normal='')
        box.add_widget(btn)

        popup = Popup(title=title, content=box, size_hint=(0.8, 0.5))
        btn.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    RestaurantPOSApp().run()
