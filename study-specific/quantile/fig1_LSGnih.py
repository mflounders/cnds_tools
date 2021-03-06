import gl
gl.resetdefaults()
#open background image
gl.loadimage('mni152')
gl.backcolor(255, 255, 255)
#open overlay: 
gl.overlayloadsmooth(0)

#open overlay: sub 41, 1 site
# n/a 

#open overlay: 
gl.overlayloadsmooth(0)
gl.overlaycloseall()

#open overlay: sub 81, 1 site
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/081sph_bin.nii.gz')
gl.minmax(1, 0,14)
gl.colorname(1,"NIH")

#open overlay: sub 111, 3 sites
# n.a

#open overlay: sub 91, 1 site
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/091sph_bin.nii.gz')
gl.minmax(2, 0,14)
gl.colorname(2,"NIH")

#open overlay: sub 121, 7 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/121sph_bin.nii.gz')
gl.minmax(3, 0,14)
gl.colorname(3,"NIH")

#open overlay: sub 201, 4 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/201sph_bin.nii.gz')
gl.minmax(4, 0,14)
gl.colorname(4,"NIH")

#open overlay: sub 211, 4 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/211sph_bin.nii.gz')
gl.minmax(5, 0,14)
gl.colorname(5,"NIH")

#open overlay: sub 241, 2 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/241sph_bin.nii.gz')
gl.minmax(6, 0,14)
gl.colorname(6,"NIH")

#open overlay: sub 271, 1 site
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/271sph_bin.nii.gz')
gl.minmax(7, 0,14)
gl.colorname(7,"NIH")

#open overlay: sub 281, 8 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/281sph_bin.nii.gz')
gl.minmax(8, 0,14)
gl.colorname(8,"NIH")

#open overlay: sub 291, 2 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/291sph_bin.nii.gz')
gl.minmax(9, 0,14)
gl.colorname(9,"NIH")

#open overlay: sub 300, 5 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/300sph_bin.nii.gz')
gl.minmax(10, 0,14)
gl.colorname(10,"NIH")

#open overlay: sub 301, 1 site
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/301sph_bin.nii.gz')
gl.minmax(11, 0,14)
gl.colorname(11,"NIH")

#open overlay: sub 321, 6 sites
gl.overlayload('/Users/mflounders/Desktop/cnds/multiplied_LSG/321sph_bin.nii.gz')
gl.minmax(12, 0,14)
gl.colorname(12,"NIH")

#shader settings
gl.shadername('Standard')
