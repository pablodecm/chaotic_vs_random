c = get_config()

c.NbConvertApp.notebooks = ['chaotic_vs_random.ipynb']
c.NbConvertApp.export_format = 'pdf'

c.Exporter.template_file = 'chaotic_vs_random'
