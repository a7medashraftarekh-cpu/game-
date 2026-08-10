[app]
title = Restaurant POS - A7MED ASHRAF
package.name = restaurantpos
package.domain = org.a7medashraf
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,sqlite3
orientation = landscape
fullscreen = 0
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.arch = arm64-v8a
icon.filename = %(source.dir)s/icon.png
[buildozer]
log_level = 2
warn_on_root = 1
