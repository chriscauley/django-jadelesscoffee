from django.conf import settings
from os import path,system
import os

def compile_all():
    #if the JLC_DIRS is set then just do them
    if hasattr(settings, 'JLC_DIRS'):
        if isinstance(settings.JLC_DIRS, tuple):
            try:
                for jlcsource, jlcdestination in settings.JLC_DIRS:
                    compile_jlc(path.normpath(jlcsource), path.normpath(jlcdestination))
            except:
                print("Cannot compile jlc directories. JLC_DIRS should be a tuple of tuples. \ne.g. JLC_DIRS = (\n    ('/path/to/src', '/path/to/'),\n    ('/path/to/other/src', '/path/to/other'),\n)")
        else:
            try:
                jlcsource, jlcdestination = settings.JLC_DIRS
                compile_jlc(path.normpath(jlcsource), path.normpath(jlcdestination))
            except:
                print("Cannot compile jlc directories. JLC_DIRS should be a tuple of tuples. \ne.g. JLC_DIRS = (\n    ('/path/to/src', '/path/to/'),\n    ('/path/to/other/src', '/path/to/other'),\n)")
        return

        
    #for each template directory look for a src dir
    if (isinstance(settings.TEMPLATE_DIRS, tuple)):
        for template_directory in settings.TEMPLATE_DIRS:
            compile_jlc(path.normpath(template_directory + '/src'), template_directory)
    else:
        compile_jlc(path.normpath(settings.TEMPLATE_DIRS + '/src'), settings.TEMPLATE_DIRS)

    #same with settings.STATICFILES_DIRS
    if (isinstance(settings.STATICFILES_DIRS, tuple)):
        for template_directory in settings.STATICFILES_DIRS:
            compile_jlc(path.normpath(template_directory + '/src'), template_directory)
    else:
        compile_jlc(path.normpath(settings.STATICFILES_DIRS + '/src'), settings.STATICFILES_DIRS)

    #settings.STATIC_ROOT shouldn't be left out.
    compile_jlc(path.normpath(settings.STATIC_ROOT + '/src'), settings.STATIC_ROOT)
        

def compile_jlc(source_directory, output_directory):
    if not path.exists(source_directory):
        #print('No such file or directory: "%s"' % source_directory)
        return
    if not path.exists(output_directory):
        #print('No such file or directory: "%s"' % output_directory)
        return

    # subprocess suddenly stopped working...
    #from subprocess import Popen, call, PIPE
    #shell=True is necessary on windows due to jlc being provided by environment variables in node
    #call(['jlc', '--incremental', '--out', output_directory, source_directory], shell=True)#, stdout=PIPE, stderr=PIPE)
    system('jlc --quiet --incremental --out "%s" "%s"' % (output_directory, source_directory))