# Generated by Django 2.2.4 on 2019-08-11 15:40

from django.db import migrations
import optin.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20190805_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpostpage',
            name='body',
            field=wagtail.core.fields.StreamField([('Heading', wagtail.core.blocks.CharBlock(classname='full title')), ('Rich_Text', wagtail.core.blocks.RichTextBlock()), ('Text', wagtail.core.blocks.TextBlock()), ('Image', wagtail.images.blocks.ImageChooserBlock(icon='image')), ('Embedded_Video', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('HTML', wagtail.core.blocks.RawHTMLBlock()), ('Quote', wagtail.core.blocks.BlockQuoteBlock()), ('Email', wagtail.core.blocks.EmailBlock()), ('Optin', optin.blocks.OptinChooserBlock('optin.Optin')), ('Code', wagtail.core.blocks.StructBlock([('language', wagtail.core.blocks.ChoiceBlock(choices=[('abap', 'ABAP'), ('abnf', 'Augmented Backus–Naur form'), ('actionscript', 'ActionScript'), ('ada', 'Ada'), ('apacheconf', 'Apache Configuration'), ('apl', 'APL'), ('applescript', 'AppleScript'), ('arduino', 'Arduino'), ('arff', 'ARFF'), ('asciidoc', 'AsciiDoc'), ('asm6502', '6502 Assembly'), ('aspnet', 'ASP.NET (C#)'), ('autohotkey', 'AutoHotkey'), ('autoit', 'AutoIt'), ('bash', 'Bash + Shell'), ('basic', 'BASIC'), ('batch', 'Batch'), ('bison', 'Bison'), ('bnf', 'Backus–Naur form + Routing Backus–Naur form'), ('brainfuck', 'Brainfuck'), ('bro', 'Bro'), ('c', 'C'), ('clike', 'C-like'), ('csharp', 'C#'), ('cpp', 'C++'), ('cil', 'CIL'), ('coffeescript', 'CoffeeScript'), ('clojure', 'Clojure'), ('crystal', 'Crystal'), ('csp', 'Content-Security-Policy'), ('css', 'CSS'), ('css-extras', 'CSS Extras'), ('d', 'D'), ('dart', 'Dart'), ('diff', 'Diff'), ('django', 'Django/Jinja2'), ('docker', 'Docker'), ('ebnf', 'Extended Backus–Naur form'), ('eiffel', 'Eiffel'), ('ejs', 'EJS'), ('elixir', 'Elixir'), ('elm', 'Elm'), ('erb', 'ERB'), ('erlang', 'Erlang'), ('fsharp', 'F#'), ('flow', 'Flow'), ('fortran', 'Fortran'), ('gcode', 'G-code'), ('gedcom', 'GEDCOM'), ('gherkin', 'Gherkin'), ('git', 'Git'), ('glsl', 'GLSL'), ('gml', 'GameMaker Language'), ('go', 'Go'), ('graphql', 'GraphQL'), ('groovy', 'Groovy'), ('haml', 'Haml'), ('handlebars', 'Handlebars'), ('haskell', 'Haskell'), ('haxe', 'Haxe'), ('hcl', 'HCL'), ('http', 'HTTP'), ('hpkp', 'HTTP Public-Key-Pins'), ('hsts', 'HTTP Strict-Transport-Security'), ('ichigojam', 'IchigoJam'), ('icon', 'Icon'), ('inform7', 'Inform 7'), ('ini', 'Ini'), ('io', 'Io'), ('j', 'J'), ('java', 'Java'), ('javadoc', 'JavaDoc'), ('javadoclike', 'JavaDoc-like'), ('javascript', 'JavaScript'), ('javastacktrace', 'Java stack trace'), ('jolie', 'Jolie'), ('jsdoc', 'JSDoc'), ('js-extras', 'JS Extras'), ('json', 'JSON'), ('jsonp', 'JSONP'), ('json5', 'JSON5'), ('julia', 'Julia'), ('keyman', 'Keyman'), ('kotlin', 'Kotlin'), ('latex', 'LaTeX'), ('less', 'Less'), ('liquid', 'Liquid'), ('lisp', 'Lisp'), ('livescript', 'LiveScript'), ('lolcode', 'LOLCODE'), ('lua', 'Lua'), ('makefile', 'Makefile'), ('markdown', 'Markdown'), ('markup', 'Markup + HTML + XML + SVG + MathML'), ('markup-templating', 'Markup templating'), ('matlab', 'MATLAB'), ('mel', 'MEL'), ('mizar', 'Mizar'), ('monkey', 'Monkey'), ('n1ql', 'N1QL'), ('n4js', 'N4JS'), ('nand2tetris-hdl', 'Nand To Tetris HDL'), ('nasm', 'NASM'), ('nginx', 'nginx'), ('nim', 'Nim'), ('nix', 'Nix'), ('nsis', 'NSIS'), ('objectivec', 'Objective-C'), ('ocaml', 'OCaml'), ('opencl', 'OpenCL'), ('oz', 'Oz'), ('parigp', 'PARI/GP'), ('parser', 'Parser'), ('pascal', 'Pascal + Object Pascal'), ('perl', 'Perl'), ('php', 'PHP'), ('phpdoc', 'PHPDoc'), ('php-extras', 'PHP Extras'), ('plsql', 'PL/SQL'), ('powershell', 'PowerShell'), ('processing', 'Processing'), ('prolog', 'Prolog'), ('properties', '.properties'), ('protobuf', 'Protocol Buffers'), ('pug', 'Pug'), ('puppet', 'Puppet'), ('pure', 'Pure'), ('python', 'Python'), ('q', 'Q (kdb+ database)'), ('qore', 'Qore'), ('r', 'R'), ('jsx', 'React JSX'), ('tsx', 'React TSX'), ('renpy', "Ren'py"), ('reason', 'Reason'), ('regex', 'Regex'), ('rest', 'reST (reStructuredText)'), ('rip', 'Rip'), ('roboconf', 'Roboconf'), ('ruby', 'Ruby'), ('rust', 'Rust'), ('sas', 'SAS'), ('sass', 'Sass (Sass)'), ('scss', 'Sass (Scss)'), ('scala', 'Scala'), ('scheme', 'Scheme'), ('smalltalk', 'Smalltalk'), ('smarty', 'Smarty'), ('sql', 'SQL'), ('soy', 'Soy (Closure Template)'), ('stylus', 'Stylus'), ('swift', 'Swift'), ('tap', 'TAP'), ('tcl', 'Tcl'), ('textile', 'Textile'), ('toml', 'TOML'), ('tt2', 'Template Toolkit 2'), ('twig', 'Twig'), ('typescript', 'TypeScript'), ('t4-cs', 'T4 Text Templates (C#)'), ('t4-vb', 'T4 Text Templates (VB)'), ('t4-templating', 'T4 templating'), ('vala', 'Vala'), ('vbnet', 'VB.Net'), ('velocity', 'Velocity'), ('verilog', 'Verilog'), ('vhdl', 'VHDL'), ('vim', 'vim'), ('visual-basic', 'Visual Basic'), ('wasm', 'WebAssembly'), ('wiki', 'Wiki markup'), ('xeora', 'Xeora + XeoraCube'), ('xojo', 'Xojo (REALbasic)'), ('xquery', 'XQuery'), ('yaml', 'YAML')], help_text='Coding language', identifier='language', label='Language')), ('code', wagtail.core.blocks.TextBlock(identifier='code', label='Code'))], label='Code Editor'))], blank=True, null=True),
        ),
    ]
