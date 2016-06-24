
params.mk: params.txt
	sed -e 'sI^I-D'\'I -e 'sI$$I'\'I -e '1sI^IPARAMS=I' $< | tr '\\\n' ' ' >$@

sinclude params.mk

%.stl: %.scad params.mk
	openscad $(PARAMS) -o $@ $<

%.dxf: %.scad params.mk
	openscad $(PARAMS) -o $@ $<

%.png: %.scad params.mk
	openscad $(PARAMS) -o $@ $<
