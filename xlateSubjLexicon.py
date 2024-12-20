import csv
import sys
import json

fldmap = {
    'word1': 'word',
    'pos1': 'partOfSpeech',
    'stemmed1': 'isStemmed',
    'priorpolarity': 'sentiment'
}
records = []
with open(sys.argv[1]) as f:
    reader = csv.reader(f, delimiter=' ')
    for row in reader:
        rec = {}
        for fld in row:
            elts = fld.split('=')
            if len(elts) == 2:
                name, value = elts
                if name in fldmap:
                    name = fldmap[name]
                rec[name] = value
            else:
                if not '_unparsed' in rec:
                    rec['_unparsed'] = []
                rec['_unparsed'].append(fld)
        rec['_raw'] = row
        records.append(rec)

print(json.dumps(records))

