relative_assets = true

line_comments = (environment == :production) ? false : true

sass_options = (environment == :production) ? {} : {:debug_info => true}

Sass::Script::Number.precision = 10


# add_import_path 'sass'
add_import_path 'bower_components'

asset_cache_buster = :none
