# -*- coding: utf-8 -*-
"""生成开题报告 Word 版本（数学公式转为 Unicode 数学字符，避免乱码）。"""
import re
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

SRC = "开题报告-基于三维点云配准的免示教焊接关键技术研究与系统实现.md"
OUT = "开题报告-基于三维点云配准的免示教焊接关键技术研究与系统实现.docx"

doc = Document()
sec = doc.sections[0]
sec.page_height = Cm(29.7)
sec.page_width = Cm(21.0)
sec.top_margin = Cm(2.54)
sec.bottom_margin = Cm(2.54)
sec.left_margin = Cm(2.7)
sec.right_margin = Cm(2.7)

body_font = doc.styles["Normal"].font
body_font.name = "Times New Roman"
body_font.size = Pt(12)
ef = doc.styles["Normal"].element.rPr.rFonts
ef.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ascii", "Times New Roman")
ef.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hAnsi", "Times New Roman")
ef.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}cs", "Times New Roman")

pstyle = doc.styles["Normal"].paragraph_format
pstyle.space_before = Pt(0)
pstyle.space_after = Pt(0)
pstyle.line_spacing = 1.5
pstyle.alignment = WD_ALIGN_PARAGRAPH.LEFT

SUB = {c: {'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉',
           'a':'ₐ','b':'ᵦ','c':'𝒄','d':'𝒅','e':'ₑ','f':'ᶠ','g':'g','h':'ₕ','i':'ᵢ','j':'ⱼ',
           'k':'ₖ','l':'ₗ','m':'ₘ','n':'ₙ','o':'ₒ','p':'ₚ','q':'𝓆','r':'ᵣ','s':'ₛ','t':'ₜ',
           'u':'ᵤ','v':'ᵥ','w':'w','x':'ₓ','y':'ᵧ','z':'ᵨ'}[c] for c in "0123456789abcdefghijklmnopqrstuvwxyz"}
SUP = {c: {'0':'⁰','1':'¹','2':'²','3':'³','4':'⁴','5':'⁵','6':'⁶','7':'⁷','8':'⁸','9':'⁹',
           'a':'ᵃ','b':'ᵇ','c':'ᶜ','d':'ᵈ','e':'ᵉ','f':'ᶠ','g':'ᵍ','h':'ʰ','i':'ⁱ','j':'ʲ',
           'k':'ᵏ','l':'ˡ','m':'ᵐ','n':'ⁿ','o':'ᵒ','p':'ᵖ','q':'ᵔ','r':'ʳ','s':'ˢ','t':'ᵗ',
           'u':'ᵘ','v':'ᵛ','w':'ʷ','x':'ˣ','y':'ʸ','z':'ᶻ'}[c] for c in "0123456789abcdefghijklmnopqrstuvwxyz"}
GREEK = {'alpha':'α','beta':'β','gamma':'γ','delta':'δ','epsilon':'ε','zeta':'ζ','eta':'η',
         'theta':'θ','iota':'ι','kappa':'κ','lambda':'λ','mu':'μ','nu':'ν','xi':'ξ','pi':'π',
         'rho':'ρ','sigma':'σ','tau':'τ','upsilon':'υ','phi':'φ','chi':'χ','psi':'ψ','omega':'ω',
         'Alpha':'Α','Beta':'Β','Gamma':'Γ','Delta':'Δ','Epsilon':'Ε','Zeta':'Ζ','Eta':'Η',
         'Theta':'Θ','Iota':'Ι','Kappa':'Κ','Lambda':'Λ','Mu':'Μ','Nu':'Ν','Xi':'Ξ','Pi':'Π',
         'Rho':'Ρ','Sigma':'Σ','Tau':'Τ','Upsilon':'Υ','Phi':'Φ','Chi':'Χ','Psi':'Ψ','Omega':'Ω'}

def sub(s):
    return ''.join(SUB.get(c, c) for c in s)

def sup(s):
    return ''.join(SUP.get(c, c) for c in s)

def math_latex_to_unicode(s):
    # \frac{a}{b} -> (a)/(b)
    s = re.sub(r'\\frac\{([^{}]*)\}\{([^{}]*)\}', lambda m: f'({m.group(1)})/({m.group(2)})', s)
    # \sqrt{a} -> √(a)
    s = re.sub(r'\\sqrt\{([^{}]*)\}', lambda m: '√(' + m.group(1) + ')', s)
    # \sum_{a}^{b} -> ∑_a^b (sub/sup applied to group)
    s = re.sub(r'\\sum\_\{([^{}]*)\}\^\{([^{}]*)\}', lambda m: '∑' + sub(m.group(1)) + sup(m.group(2)), s)
    s = re.sub(r'\\sum', '∑', s)
    s = re.sub(r'\\prod', '∏', s)
    s = re.sub(r'\\int', '∫', s)
    s = re.sub(r'\\lim', 'lim', s)
    s = re.sub(r'\\min', 'min', s)
    s = re.sub(r'\\max', 'max', s)
    s = re.sub(r'\\log', 'log', s)
    s = re.sub(r'\\ln', 'ln', s)
    s = re.sub(r'\\pm', '±', s)
    s = re.sub(r'\\times', '×', s)
    s = re.sub(r'\\div', '÷', s)
    s = re.sub(r'\\cdot', '·', s)
    s = re.sub(r'\\ldots', '…', s)
    s = re.sub(r'\\cdots', '⋯', s)
    s = re.sub(r'\\in', '∈', s)
    s = re.sub(r'\\infty', '∞', s)
    s = re.sub(r'\\partial', '∂', s)
    s = re.sub(r'\\nabla', '∇', s)
    s = re.sub(r'\\approx', '≈', s)
    s = re.sub(r'\\sim', '∼', s)
    s = re.sub(r'\\equiv', '≡', s)
    s = re.sub(r'\\neq', '≠', s)
    s = re.sub(r'\\leq', '≤', s)
    s = re.sub(r'\\geq', '≥', s)
    s = re.sub(r'\\ll', '≪', s)
    s = re.sub(r'\\gg', '≫', s)
    s = re.sub(r'\\mathbb\{([a-zA-Z])\}', lambda m: {'R':'ℝ','Z':'ℤ','N':'ℕ','C':'ℂ'}.get(m.group(1), m.group(1)), s)
    s = re.sub(r'\\mathcal\{([^{}]*)\}', lambda m: GREEK.get(m.group(1), m.group(1)), s)
    s = re.sub(r'\\operatorname\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\left\{([^\\]*)\\right\}', lambda m: '{' + m.group(1) + '}', s)
    s = re.sub(r'\\left\(', lambda m: '(', s)
    s = re.sub(r'\\left\]', lambda m: '[', s)
    s = re.sub(r'\\right\)', lambda m: ')', s)
    s = re.sub(r'\\right\]', lambda m: ']', s)
    s = re.sub(r'\\text\{([^{}]*)\}', r'\1', s)
    s = re.sub(r'\\quad', '    ', s)
    s = re.sub(r'\\,', ' ', s)
    s = re.sub(r'\\\|', '‖', s)
    # 处理 \bar{a}, \hat{a}, \vec{a}, \dot{a}, \ddot{a}, \tilde{a}, \overline{a}
    s = re.sub(r'\\bar\{([^{}]*)\}', lambda m: m.group(1) + '̄', s)
    s = re.sub(r'\\hat\{([^{}]*)\}', lambda m: m.group(1) + '̂', s)
    s = re.sub(r'\\dot\{([^{}]*)\}', lambda m: m.group(1) + '̇', s)
    s = re.sub(r'\\ddot\{([^{}]*)\}', lambda m: m.group(1) + '̈', s)
    s = re.sub(r'\\vec\{([^{}]*)\}', lambda m: m.group(1) + '⃗', s)
    s = re.sub(r'\\overline\{([^{}]*)\}', lambda m: m.group(1) + '̄', s)
    # 裸下标 _text 和上标 ^text（MD 里常用 _i、^2 这种写法）
    def _bare_sup(m):
        g = m.group(1)
        return sup(g) if all(c in SUP for c in g) else m.group(0)
    def _bare_sub(m):
        g = m.group(1)
        return sub(g) if all(c in SUB for c in g) else m.group(0)
    s = re.sub(r'\^\{([^{}]*)\}', lambda m: sup(m.group(1)), s)
    s = re.sub(r'_\{([^{}]*)\}', lambda m: sub(m.group(1)), s)
    s = re.sub(r'\^([^{}\s]+)', _bare_sup, s)
    s = re.sub(r'_([^{}\s]+)', _bare_sub, s)
    return s

def render_matrix(rows, sep='&'):
    return '\n'.join('  '.join(c.strip() for c in r.split(sep)) for r in rows if r.strip())

def convert_inline_latex(s):
    """行内 $...$ 转 Unicode 数学字符。"""
    def repl(m):
        return math_latex_to_unicode(m.group(1).strip())
    # 先处理矩阵块（\begin{bmatrix} 等），避免与 $...$ 冲突
    s = re.sub(r'\\begin\{bmatrix\}([^\\]*)\\end\{bmatrix\}', lambda m: render_matrix(m.group(1).split('\\\\'), '&'), s)
    s = re.sub(r'\\begin\{pmatrix\}([^\\]*)\\end\{pmatrix\}', lambda m: render_matrix(m.group(1).split('\\\\'), '&'), s)
    s = re.sub(r'\\\{', '{', s)
    s = re.sub(r'\\\}', '}', s)
    s = re.sub(r'\$([^$]+)\$', repl, s)
    return s

def parse_line(line):
    """返回 (bold, main_text, remaining_text)。"""
    m = re.match(r"\*\*\*(.*?)\*\*\*\*", line)
    if m:
        return True, m.group(1), line[m.end():].strip()
    m = re.match(r"\*\*(.*?)\*\*", line)
    if m:
        return True, m.group(1), line[m.end():].strip()
    return False, line, ""

def _add_run(para, text, bold):
    if not text:
        return
    run = para.add_run(text)
    run.bold = bold
    if bold:
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)
        add_cjk_font(run, "黑体")
    else:
        run.font.size = Pt(12)
        add_cjk_font(run, "仿宋_GB2312")

def add_line(bold, main, remaining):
    """bold 主段与剩余文字在同一行输出。"""
    para = doc.add_paragraph()
    para.paragraph_format.line_spacing = 1.5
    _add_run(para, main, bold)
    _add_run(para, remaining, False)
    return para

def add_display_equation(latex):
    """输出一个居中的 Unicode 方程。"""
    # 先渲染矩阵块（去掉 \begin{bmatrix} 等标记），再转 Unicode
    # 用 (.+?) 非贪婪捕获，允许跨行；行内用 \\\\ 分隔行、& 分隔列
    latex = re.sub(r'\\begin\{bmatrix\}(.+?)\\end\{bmatrix\}', lambda m: render_matrix(m.group(1).split('\\\\'), '&'), latex, flags=re.DOTALL)
    latex = re.sub(r'\\begin\{pmatrix\}(.+?)\\end\{pmatrix\}', lambda m: render_matrix(m.group(1).split('\\\\'), '&'), latex, flags=re.DOTALL)
    para = doc.add_paragraph()
    para.paragraph_format.line_spacing = 1.5
    para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = para.add_run(math_latex_to_unicode(latex))
    run.font.name = "Times New Roman"
    run.font.size = Pt(12)
    run.bold = True
    add_cjk_font(run, "Times New Roman")
    return para

def add_heading(text, level):
    para = doc.add_paragraph()
    para.paragraph_format.space_before = Pt(12 if level == 1 else 8)
    para.paragraph_format.space_after = Pt(6 if level == 1 else 4)
    para.paragraph_format.line_spacing = 1.5
    run = para.add_run(text)
    if level == 1:
        run.font.size = Pt(18)   # 小二号
        add_cjk_font(run, "黑体")
    elif level == 2:
        run.font.size = Pt(16)   # 三号
        add_cjk_font(run, "黑体")
    else:
        run.font.size = Pt(15)   # 小三
        add_cjk_font(run, "黑体")
    run.bold = True
    return para

def add_cjk_font(run, font_name):
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(r"{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts")
    if rfonts is None:
        rfonts = rpr.makeelement(r"{http://schemas.openxmlformats.org/wordprocessingml/2006/main}rFonts", {})
        rpr.append(rfonts)
    rfonts.set("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}eastAsia", font_name)

def render_matrix_block(block):
    return render_matrix(block.split('\\\\'), '&')

with open(SRC, encoding="utf-8") as f:
    lines = f.read().splitlines()

i = 0
while i < len(lines):
    line = lines[i].rstrip()
    if not line.strip():
        i += 1
        continue
    m = re.match(r"^(#{1,4})\s+(.+)$", line)
    if m:
        level = len(m.group(1))
        add_heading(m.group(2), 3 if level == 3 else level)
        i += 1
        continue
    m = re.match(r"^\$\$([^$]*)\$\$$", line)
    if m:
        add_display_equation(m.group(1).strip())
        i += 1
        continue
    # 多行 $...$ 块：当前行以 $$ 开头（且不是行内 $）时，合并后续行
    m = re.match(r"^\$\$", line)
    if m:
        buf = [line[2:]]  # 去掉开头的两个 $
        i += 1
        # 读到包含 $ 的行即停止（闭合标记）
        while i < len(lines) and '$' not in lines[i]:
            buf.append(lines[i])
            i += 1
        if i < len(lines):
            add_display_equation("".join(buf).strip())
        i += 1
        continue
    line = convert_inline_latex(line)
    bold, main, remaining = parse_line(line)
    add_line(bold, main, remaining)
    i += 1

doc.save(OUT)
print("saved", OUT)
