score = int(input('masukan score : '))
if (score >= 90 and score <= 100):
    nilai = 'A'
    predikat = 'dengan pujian'
elif (score >= 80 and score < 90):
    nilai = 'B'
    predikat = 'sangat memuaskan'
elif (score >= 70 and score < 79):
    nilai = 'C'
    predikat = 'memuaskan'
elif (score >= 60 and score < 69):
    nilai = 'D'
    predikat = 'tidak memuaskan'
elif (score >= 0 and score < 59):
    nilai = 'E'
    predikat = 'tidak lulus'
else:
    print ('error')
print ('score anda:', score,'nilai', nilai, 'predikat',predikat)