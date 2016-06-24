
params.mk: params.txt
	sed -e 's/^/-D/' -e '1s/^/PARAMS=/' $< | tr '\\n' ' ' >$@

sinclude params.mk

%.stl: %.scad
	openscad $(PARAMS) -o $@ $<

%.png: %.scad
	openscad $(PARAMS) -o $@ $<
