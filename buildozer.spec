[app]

# एपको नाम र प्याकेज जानकारी
title = NARESH AV TOOLBOX
package.name = avtool
package.domain = org.nkushmi

# स्रोत फाइलहरू (main.py भएको ठाउँ)
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0

# आवश्यक लाइब्रेरीहरू (ffmpeg र ffprobe थपिएको छ)
requirements = python3, kivy, ffmpeg, ffprobe, android

# एन्ड्रोइड सेटिङहरू (AIDL को लागि ३४.०.० अनिवार्य छ)
android.api = 34
android.minapi = 21
android.sdk = 34
android.build_tools_version = 34.0.0
android.accept_sdk_license = True
android.skip_update = False

# पर्मिसनहरू (Storage Permission)
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# स्क्रिन सेटिङ
orientation = portrait
fullscreen = 1

# बिल्डोजर सेटिङ
log_level = 2
warn_on_root = 1

[buildozer]
bin_dir = ./bin
