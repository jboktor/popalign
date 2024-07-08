from distutils.core import setup

setup(
	name="popalign",
	version="0.1",
	author="Paul Rivaud",
	author_email="paulrivaud.info@gmail.com",
	keywords="popalign",
	packages=[
		"popalign",
	],
	package_dirs={"popalign":"popalign"},
	package_data={"popalign":["gsea/*.npy"]},
	install_requires=[
		"numpy",
		"pandas",
		"scipy",
		"scikit-learn",
		"plotly",
		"matplotlib",
		"seaborn",
		"adjustText",
		"ipywidgets",
		"fastcluster",
		"umap-learn",
	]
)
