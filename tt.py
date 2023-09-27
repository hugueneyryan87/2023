habitantes =0
total_paisA=0
total_paisB=0
ano =1
    while paisA <= paisB:
        paisA = 5000000
        paisB = 7000000
        ano+=1
        total_paisA =(paisA+(paisA +0.3)/100)
        total_paisB =(paisB+(paisB +0.2)/100)
        if paisA > paisB:
        print(f'Será Preciso {ano} Anos, Para o Pais A ser Maior que Pais B: ') 