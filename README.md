# ConvertMD2Doc

#### Useage

首先请确保安装了`markdown`, `pypandoc`.

`Pygments`可以生成高亮代码.

```
pip install markdown
pip install pypandoc

# optional
pip install Pygments
```

**生成默认的css文件**

`pygmentize -S default -f html > default.css`

```
python convertMD2Doc.py test.md test.html
```
