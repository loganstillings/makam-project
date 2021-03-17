usulAverages = {}

with open(makamDistribution) as json_file:
    data = json.load(json_file)
    for makam in data.keys():
        usulAverages[makam] = {}
        tmp_keys = []
        tmp_vals = []
        usuls = []
        for i, usul in enumerate(data[makam]['usuls']):
            keys = np.fromiter(data[makam]['usuls'][usul].keys(), dtype='U20')
            vals = np.fromiter(data[makam]['usuls'][usul].values(), dtype=float)
            tmp_keys.append(keys)
            tmp_vals.append(vals)
            usuls.append(usul)
        list_of_keys, vals_norm = set_up_data(tmp_keys,tmp_vals)
        for i, pitch in enumerate(list_of_keys):
            usulAverages[makam][pitch] = 0
            for j in range(len(vals_norm)):
                usulAverages[makam][pitch] += vals_norm[j][i]
            usulAverages[makam][pitch] /= len(vals_norm)
print(usulAverages)