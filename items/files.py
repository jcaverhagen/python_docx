
class StyleFile :

	def __init__(self) :
		self.dirName = 'word'
		self.fileName = 'styles.xml'
		self.xml_string = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
			<w:styles xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
			<w:docDefaults>
			<w:rPrDefault>
			<w:rPr>
			<w:rFonts w:asciiTheme="minorHAnsi" w:eastAsiaTheme="minorHAnsi" w:hAnsiTheme="minorHAnsi" w:cstheme="minorBidi"/>
			<w:sz w:val="22"/>
			<w:szCs w:val="22"/>
			<w:lang w:val="nl-NL" w:eastAsia="en-US" w:bidi="ar-SA"/>
			</w:rPr>
			</w:rPrDefault>
			<w:pPrDefault>
			<w:pPr>
			<w:spacing w:after="200" w:line="276" w:lineRule="auto"/>
			</w:pPr>
			</w:pPrDefault>
			</w:docDefaults>
			<w:latentStyles w:defLockedState="0" w:defUIPriority="99" w:defSemiHidden="1" w:defUnhideWhenUsed="1" w:defQFormat="0" w:count="267">
			<w:lsdException w:name="Normal" w:semiHidden="0" w:uiPriority="0" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="heading 1" w:semiHidden="0" w:uiPriority="9" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="heading 2" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 3" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 4" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 5" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 6" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 7" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 8" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="heading 9" w:uiPriority="9" w:qFormat="1"/>
			<w:lsdException w:name="toc 1" w:uiPriority="39"/>
			<w:lsdException w:name="toc 2" w:uiPriority="39"/>
			<w:lsdException w:name="toc 3" w:uiPriority="39"/>
			<w:lsdException w:name="toc 4" w:uiPriority="39"/>
			<w:lsdException w:name="toc 5" w:uiPriority="39"/>
			<w:lsdException w:name="toc 6" w:uiPriority="39"/>
			<w:lsdException w:name="toc 7" w:uiPriority="39"/>
			<w:lsdException w:name="toc 8" w:uiPriority="39"/>
			<w:lsdException w:name="toc 9" w:uiPriority="39"/>
			<w:lsdException w:name="caption" w:uiPriority="35" w:qFormat="1"/>
			<w:lsdException w:name="Title" w:semiHidden="0" w:uiPriority="10" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Default Paragraph Font" w:uiPriority="1"/>
			<w:lsdException w:name="Subtitle" w:semiHidden="0" w:uiPriority="11" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Strong" w:semiHidden="0" w:uiPriority="22" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Emphasis" w:semiHidden="0" w:uiPriority="20" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Table Grid" w:semiHidden="0" w:uiPriority="59" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Placeholder Text" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="No Spacing" w:semiHidden="0" w:uiPriority="1" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Light Shading" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 2" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Shading Accent 1" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List Accent 1" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid Accent 1" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1 Accent 1" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2 Accent 1" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1 Accent 1" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Revision" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="List Paragraph" w:semiHidden="0" w:uiPriority="34" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Quote" w:semiHidden="0" w:uiPriority="29" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Intense Quote" w:semiHidden="0" w:uiPriority="30" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Medium List 2 Accent 1" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1 Accent 1" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2 Accent 1" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3 Accent 1" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List Accent 1" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading Accent 1" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List Accent 1" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid Accent 1" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Shading Accent 2" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List Accent 2" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid Accent 2" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1 Accent 2" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2 Accent 2" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1 Accent 2" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 2 Accent 2" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1 Accent 2" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2 Accent 2" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3 Accent 2" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List Accent 2" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading Accent 2" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List Accent 2" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid Accent 2" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Shading Accent 3" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List Accent 3" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid Accent 3" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1 Accent 3" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2 Accent 3" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1 Accent 3" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 2 Accent 3" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1 Accent 3" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2 Accent 3" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3 Accent 3" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List Accent 3" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading Accent 3" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List Accent 3" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid Accent 3" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Shading Accent 4" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List Accent 4" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid Accent 4" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1 Accent 4" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2 Accent 4" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1 Accent 4" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 2 Accent 4" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1 Accent 4" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2 Accent 4" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3 Accent 4" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List Accent 4" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading Accent 4" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List Accent 4" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid Accent 4" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Shading Accent 5" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List Accent 5" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid Accent 5" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1 Accent 5" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2 Accent 5" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1 Accent 5" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 2 Accent 5" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1 Accent 5" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2 Accent 5" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3 Accent 5" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List Accent 5" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading Accent 5" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List Accent 5" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid Accent 5" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Shading Accent 6" w:semiHidden="0" w:uiPriority="60" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light List Accent 6" w:semiHidden="0" w:uiPriority="61" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Light Grid Accent 6" w:semiHidden="0" w:uiPriority="62" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 1 Accent 6" w:semiHidden="0" w:uiPriority="63" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Shading 2 Accent 6" w:semiHidden="0" w:uiPriority="64" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 1 Accent 6" w:semiHidden="0" w:uiPriority="65" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium List 2 Accent 6" w:semiHidden="0" w:uiPriority="66" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 1 Accent 6" w:semiHidden="0" w:uiPriority="67" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 2 Accent 6" w:semiHidden="0" w:uiPriority="68" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Medium Grid 3 Accent 6" w:semiHidden="0" w:uiPriority="69" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Dark List Accent 6" w:semiHidden="0" w:uiPriority="70" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Shading Accent 6" w:semiHidden="0" w:uiPriority="71" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful List Accent 6" w:semiHidden="0" w:uiPriority="72" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Colorful Grid Accent 6" w:semiHidden="0" w:uiPriority="73" w:unhideWhenUsed="0"/>
			<w:lsdException w:name="Subtle Emphasis" w:semiHidden="0" w:uiPriority="19" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Intense Emphasis" w:semiHidden="0" w:uiPriority="21" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Subtle Reference" w:semiHidden="0" w:uiPriority="31" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Intense Reference" w:semiHidden="0" w:uiPriority="32" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Book Title" w:semiHidden="0" w:uiPriority="33" w:unhideWhenUsed="0" w:qFormat="1"/>
			<w:lsdException w:name="Bibliography" w:uiPriority="37"/>
			<w:lsdException w:name="TOC Heading" w:uiPriority="39" w:qFormat="1"/>
			</w:latentStyles>
			<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
			<w:name w:val="Normal"/>
			<w:qFormat/>
			<w:rsid w:val="00A42688"/>
			</w:style>
			<w:style w:type="paragraph" w:styleId="Heading1">
			<w:name w:val="heading 1"/>
			<w:basedOn w:val="Normal"/>
			<w:next w:val="Normal"/>
			<w:link w:val="Heading1Char"/>
			<w:uiPriority w:val="9"/>
			<w:qFormat/>
			<w:rsid w:val="00EE745C"/>
			<w:pPr>
			<w:keepNext/>
			<w:keepLines/>
			<w:spacing w:before="480" w:after="0"/>
			<w:outlineLvl w:val="0"/>
			</w:pPr>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:color w:val="365F91" w:themeColor="accent1" w:themeShade="BF"/>
			<w:sz w:val="28"/>
			<w:szCs w:val="28"/>
			</w:rPr>
			</w:style>
			<w:style w:type="paragraph" w:styleId="Heading2">
			<w:name w:val="heading 2"/>
			<w:basedOn w:val="Normal"/>
			<w:next w:val="Normal"/>
			<w:link w:val="Heading2Char"/>
			<w:uiPriority w:val="9"/>
			<w:unhideWhenUsed/>
			<w:qFormat/>
			<w:rsid w:val="00EE745C"/>
			<w:pPr>
			<w:keepNext/>
			<w:keepLines/>
			<w:spacing w:before="200" w:after="0"/>
			<w:outlineLvl w:val="1"/>
			</w:pPr>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:color w:val="4F81BD" w:themeColor="accent1"/>
			<w:sz w:val="26"/>
			<w:szCs w:val="26"/>
			</w:rPr>
			</w:style>
			<w:style w:type="paragraph" w:styleId="Heading3">
			<w:name w:val="heading 3"/>
			<w:basedOn w:val="Normal"/>
			<w:next w:val="Normal"/>
			<w:link w:val="Heading3Char"/>
			<w:uiPriority w:val="9"/>
			<w:unhideWhenUsed/>
			<w:qFormat/>
			<w:rsid w:val="00EE745C"/>
			<w:pPr>
			<w:keepNext/>
			<w:keepLines/>
			<w:spacing w:before="200" w:after="0"/>
			<w:outlineLvl w:val="2"/>
			</w:pPr>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:color w:val="4F81BD" w:themeColor="accent1"/>
			</w:rPr>
			</w:style>
			<w:style w:type="paragraph" w:styleId="Heading4">
			<w:name w:val="heading 4"/>
			<w:basedOn w:val="Normal"/>
			<w:next w:val="Normal"/>
			<w:link w:val="Heading4Char"/>
			<w:uiPriority w:val="9"/>
			<w:unhideWhenUsed/>
			<w:qFormat/>
			<w:rsid w:val="00EE745C"/>
			<w:pPr>
			<w:keepNext/>
			<w:keepLines/>
			<w:spacing w:before="200" w:after="0"/>
			<w:outlineLvl w:val="3"/>
			</w:pPr>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:i/>
			<w:iCs/>
			<w:color w:val="4F81BD" w:themeColor="accent1"/>
			</w:rPr>
			</w:style>
			<w:style w:type="paragraph" w:styleId="Heading5">
			<w:name w:val="heading 5"/>
			<w:basedOn w:val="Normal"/>
			<w:next w:val="Normal"/>
			<w:link w:val="Heading5Char"/>
			<w:uiPriority w:val="9"/>
			<w:unhideWhenUsed/>
			<w:qFormat/>
			<w:rsid w:val="00EE745C"/>
			<w:pPr>
			<w:keepNext/>
			<w:keepLines/>
			<w:spacing w:before="200" w:after="0"/>
			<w:outlineLvl w:val="4"/>
			</w:pPr>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:color w:val="243F60" w:themeColor="accent1" w:themeShade="7F"/>
			</w:rPr>
			</w:style>
			<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont">
			<w:name w:val="Default Paragraph Font"/>
			<w:uiPriority w:val="1"/>
			<w:semiHidden/>
			<w:unhideWhenUsed/>
			</w:style>
			<w:style w:type="table" w:default="1" w:styleId="TableNormal">
			<w:name w:val="Normal Table"/>
			<w:uiPriority w:val="99"/>
			<w:semiHidden/>
			<w:unhideWhenUsed/>
			<w:qFormat/>
			<w:tblPr>
			<w:tblInd w:w="0" w:type="dxa"/>
			<w:tblCellMar>
			<w:top w:w="0" w:type="dxa"/>
			<w:left w:w="108" w:type="dxa"/>
			<w:bottom w:w="0" w:type="dxa"/>
			<w:right w:w="108" w:type="dxa"/>
			</w:tblCellMar>
			</w:tblPr>
			</w:style>
			<w:style w:type="numbering" w:default="1" w:styleId="NoList">
			<w:name w:val="No List"/>
			<w:uiPriority w:val="99"/>
			<w:semiHidden/>
			<w:unhideWhenUsed/>
			</w:style>
			<w:style w:type="character" w:customStyle="1" w:styleId="Heading1Char">
			<w:name w:val="Heading 1 Char"/>
			<w:basedOn w:val="DefaultParagraphFont"/>
			<w:link w:val="Heading1"/>
			<w:uiPriority w:val="9"/>
			<w:rsid w:val="00EE745C"/>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:color w:val="365F91" w:themeColor="accent1" w:themeShade="BF"/>
			<w:sz w:val="28"/>
			<w:szCs w:val="28"/>
			</w:rPr>
			</w:style>
			<w:style w:type="character" w:customStyle="1" w:styleId="Heading2Char">
			<w:name w:val="Heading 2 Char"/>
			<w:basedOn w:val="DefaultParagraphFont"/>
			<w:link w:val="Heading2"/>
			<w:uiPriority w:val="9"/>
			<w:rsid w:val="00EE745C"/>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:color w:val="4F81BD" w:themeColor="accent1"/>
			<w:sz w:val="26"/>
			<w:szCs w:val="26"/>
			</w:rPr>
			</w:style>
			<w:style w:type="character" w:customStyle="1" w:styleId="Heading3Char">
			<w:name w:val="Heading 3 Char"/>
			<w:basedOn w:val="DefaultParagraphFont"/>
			<w:link w:val="Heading3"/>
			<w:uiPriority w:val="9"/>
			<w:rsid w:val="00EE745C"/>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:color w:val="4F81BD" w:themeColor="accent1"/>
			</w:rPr>
			</w:style>
			<w:style w:type="character" w:customStyle="1" w:styleId="Heading4Char">
			<w:name w:val="Heading 4 Char"/>
			<w:basedOn w:val="DefaultParagraphFont"/>
			<w:link w:val="Heading4"/>
			<w:uiPriority w:val="9"/>
			<w:rsid w:val="00EE745C"/>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:b/>
			<w:bCs/>
			<w:i/>
			<w:iCs/>
			<w:color w:val="4F81BD" w:themeColor="accent1"/>
			</w:rPr>
			</w:style>
			<w:style w:type="character" w:customStyle="1" w:styleId="Heading5Char">
			<w:name w:val="Heading 5 Char"/>
			<w:basedOn w:val="DefaultParagraphFont"/>
			<w:link w:val="Heading5"/>
			<w:uiPriority w:val="9"/>
			<w:rsid w:val="00EE745C"/>
			<w:rPr>
			<w:rFonts w:asciiTheme="majorHAnsi" w:eastAsiaTheme="majorEastAsia" w:hAnsiTheme="majorHAnsi" w:cstheme="majorBidi"/>
			<w:color w:val="243F60" w:themeColor="accent1" w:themeShade="7F"/>
			</w:rPr>
			</w:style>
			</w:styles>"""

	def getStyleFile(self) :
		return self.xml_string