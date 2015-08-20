relative_assets = true

line_comments = (environment == :production) ? false : true

sass_options = (environment == :production) ? {} : {:debug_info => true}

Sass::Script::Number.precision = 10


add_import_path 'core/static/core/styles'
add_import_path 'personal/static/personal/styles'
add_import_path 'blog/static/blog/styles'
add_import_path 'bower_components'

asset_cache_buster = :none

http_path = '/'
sass_dir = 'sass'
