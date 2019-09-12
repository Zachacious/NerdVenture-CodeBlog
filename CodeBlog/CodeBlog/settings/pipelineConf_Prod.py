# In production run collectstatic and set PIPELINE_ENABLED = True
PIPELINE = {
    'PIPELINE_ENABLED': True,
    'DISABLED_WRAPPER': True,
    'JS_COMPRESSOR': 'pipeline.compressors.slimit.SlimItCompressor',
    'JAVASCRIPT': {
        'general': {
            'source_filenames': (
                'js/notify.js',
                'js/cookies.js',
            ),
            'output_filename': 'js/general.min.js',
            'extra_context': {
                'async': True,
                'defer': True,
            },
        },
        'contact_form': {
            'source_filenames': (
                'blog/js/contactForm.js',
            ),
            'output_filename': 'blog/js/contactForm.min.js',
            'extra_context': {
                'defer': True,
            },
        },
        'optins': {
            'source_filenames': (
                'optin/js/optin.js',
            ),
            'output_filename': 'optin/js/optin.min.js',
            'extra_context': {
                'defer': True,
            },
        }
    },
    'STYLESHEETS': {
        'general': {
            'source_filenames': (
                # 'css/CodeBlog.css',
                'css/NerdVenture.css',
            ),
            'output_filename': 'css/CodeBlog.min.css',
            
        },
    },
}

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.slimit.SlimItCompressor'
