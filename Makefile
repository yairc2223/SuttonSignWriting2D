
# Getting the original SuttonSignWritingOneD ttf file
artifacts/SuttonSignWritingOneD.ttf:
	curl https://raw.githubusercontent.com/sutton-signwriting/font-ttf/master/src/font/SuttonSignWritingOneD.ttf --output $@

# Turning the original ttf font file into a ttx file in order to change it.
artifacts/SuttonSignWritingOneD.ttx: artifacts/SuttonSignWritingOneD.ttf
	ttx -o $@ artifacts/SuttonSignWritingOneD.ttf

# Correcting and changing the ttx file, second argument is proportion
artifacts/SuttonSignWritingTwoD.ttx: artifacts/SuttonSignWritingOneD.ttx Mbox-svg-replace.txt correct.py
	python correct.py artifacts/SuttonSignWritingOneD.ttx #$@

# Turning the ttx file into a TTF file
artifacts/SuttonSignWritingTwoD.ttf: artifacts/SuttonSignWritingTwoD.ttx
	ttx -o $@ artifacts/SuttonSignWritingTwoD.ttx

# Generating a vtp file for the font
artifacts/project.vtp: vtp-generator.py artifacts/SuttonSignWritingTwoD.ttf
	python vtp-generator.py artifacts/SuttonSignWritingTwoD.ttx > $@

# Add a VTP file instructions to a TTF File
artifacts/font.ttf: artifacts/project.vtp artifacts/SuttonSignWritingTwoD.ttf
	volt2ttf -t artifacts/project.vtp artifacts/SuttonSignWritingTwoD.ttf $@

# Draws the output on png
artifacts/image.png: draw.py artifacts/font.ttf
	python draw.py $@ artifacts/font.ttf

testing: artifacts/image.png original.png
	python testing.py artifacts/image.png original.png

watch:
	watch -n1 make artifacts/image.png