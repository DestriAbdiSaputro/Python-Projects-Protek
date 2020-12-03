print('======================================')
print('Mahasiswa Dengan Nilai Akhir Tertinggi')
print('======================================')
nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
def nilaiTertinggi(nilaiMhs):
    nilai = 0
    for i in nilaiMhs:
        nilaimid = i.get('mid')
        nilaiuas = i.get('uas')
        nilaiakhir = (nilaimid + 2*nilaiuas)/3
        if (nilaiakhir > nilai):
            nilai = nilaiakhir
            data = {}
            data['nim'] = i.get('nim')
            data['nama'] = i.get('nama')
    return data
nilaitinggi = nilaiTertinggi(nilaiMhs)
print('NIM Mahasiswa',nilaitinggi['nim'])
print('Nama Mahasiswa',nilaitinggi['nama'])
