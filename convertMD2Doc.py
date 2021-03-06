import markdown
import os
import sys
import pypandoc

def md2html(mdstr):
    exts = ['markdown.extensions.extra', 'markdown.extensions.codehilite','markdown.extensions.tables','markdown.extensions.toc']
    
    html = '''
        <html lang="zh-cn">
        <head>
        <meta content="text/html; charset=utf-8" http-equiv="content-type" />
        <link href="default.css" rel="stylesheet">
        <link href="github.css" rel="stylesheet">
        </head>
        <body>
        %s
        </body>
        </html>
        '''
    
    ret = markdown.markdown(mdstr,extensions=exts)
    return html % ret



if __name__ == '__main__':
    
    if len(sys.argv) < 3:
        print('usage: md2html source_filename target_file')
        sys.exit()

    infile = open(sys.argv[1],'r')
    md = infile.read()
    infile.close()


if os.path.exists(sys.argv[2]):
    os.remove(sys.argv[2])
    
# 转换 to HTML
outfile = open(sys.argv[2],'a')
outfile.write(md2html(md))
outfile.close()
# 转换  to Doc 文件
output = pypandoc.convert(source=sys.argv[2], format='html', to='docx', outputfile=sys.argv[2].split('.')[0] + '.docx', extra_args=['-RTS'])

print('convert %s to %s success!'%(sys.argv[1],sys.argv[2]))