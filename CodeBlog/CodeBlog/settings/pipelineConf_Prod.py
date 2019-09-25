# In production run collectstatic and set PIPELINE_ENABLED = True
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'DISABLED_WRAPPER': False,
    # 'JS_COMPRESSOR': 'pipeline.compressors.slimit.SlimItCompressor',
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
                # 'async': True,
                'defer': True,
            },
        },
        # 'contact_form': { 
        #     'source_filenames': (
        #         'blog/js/contactForm.js',
        #     ),
        #     'output_filename': 'blog/js/contactForm.min.js',
        #     'extra_context': {
        #         'defer': True,
        #     },
        # },
        # 'optins': {
        #     'source_filenames': (
        #         'optin/js/optin.js',
        #     ),
        #     'output_filename': 'optin/js/optin.min.js',
        #     'extra_context': {
        #         'defer': True,
        #     },
        # },
        # 'social': {
        #     'source_filenames': (
        #         'social/js/social.js',
        #     ),
        #     'output_filename': 'social/js/social.min.js',
        #     'extra_context': {
        #         # 'defer': True,
        #         # 'async': True,
        #     },
        # }
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
        },
    },
}

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.jsmin.JSMinCompressor'
PIPELINE['CSS_COMPRESSOR'] = 'pipeline.compressors.cssmin.CSSMinCompressor'