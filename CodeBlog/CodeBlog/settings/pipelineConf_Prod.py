PIPELINE = {
    'PIPELINE_ENABLED': False,
    'DISABLED_WRAPPER': True,
    'JS_COMPRESSOR': 'pipeline.compressors.jsmin.JSMinCompressor',
    'CSS_COMPRESSOR': 'pipeline.compressors.cssmin.CSSMinCompressor',
    'JAVASCRIPT': {
        'general': {
            'source_filenames': (
                'js/notify.js',
                'js/cookies.js',
                'js/header.js',
                'optin/js/optin.js',
                'blog/js/contactForm.js',
                'social/js/social.js',
                'js/progressive-image.js',
            ),
            'output_filename': 'js/general.min.js',
            'extra_context': {
                'defer': True,
            },
            'manifest': True,
        },
    },
    'STYLESHEETS': {
        'general': {
            'source_filenames': (
                # 'css/CodeBlog.css',
                'css/NerdVenture.css',
                'css/menu.css',
                'css/footer.css',
                'blog/css/blog.css',
                'social/css/social.css',
                'css/header.css',
                'css/anims.css',
            ),
            'output_filename': 'css/general.min.css',
            'manifest': True,
        },
    },
}

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor'

PIPELINE_COLLECTOR_ENABLED = True
SHOW_ERRORS_INLINE = True