import base64


class Base64(object):
    
    @classmethod
    def convertToBytes(cls, imageBase64: str) -> bytes:
        return base64.b64decode(imageBase64)
    
if __name__ == '__main__':
    
    base64_str = "/9j/4AAQSkZJRgABAgAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nICIsIxwcKDcpLDAxNDQ0Hyc5PTgyPC4zNDL/2wBDAQkJCQwLDBgNDRgyIRwhMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjIyMjL/wAARCAC+ASUDASIAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD3+ivPNS1bUJdPlW2XWIJZ550EExgZ4mwMplZDkA5IIJwGA7Vd8P63d2Wi39zqC3k32C3VmR9gYkKSQPmJyeMZxQB21FcPqV14igvb/Vfs2qWlklsh8qKS1fGzeWbDk9iOnpU+r6tqVsohtdYij2W48w3GiT3DuxGdweJ0QcEcAcEHnsADsaK4Xwrq2p3un6fBd6zHIk1oqjydGuIpQxQYbzndkyPUrg0zXZdR0fxLpVqmq65c2k9rdTTpbpC8i+W0IDAbMkASNkAEnjAoA72iuH1C6iNlpk1tr11d2lxcPula7WDpE+FLoF24YDIIyCMYzxXKXOoapB4f1W4k1PUY5LfT7qaOctcxqZlVygjJkZWA25ywGRt4OTgA9jorh/Eev3507xBFb3OnWwtN0S75mWU/u1bcMdPvcfSpdS8RahBZ6lEtxYNLHps1zHNZuWKMm0DIOR/F+lKTsrl04OpNQW7djs6K8t/te+WGCAXOvLM9zsuws0MsxHkGUeWfuKMEE+2e9Ra/4hktvDVguma1qkEt+gWOC9MJdkZjmV5D90EHAO4AYHTBrneJik3Y9eOSVZTjBSXvPz89dL9vu7Hq9FeZaHrl5LqmnaWNcvCsjeWn76yuOFUthim5uQOp596ojxbq41DUzFqFrK90lwDAWZfsQh+VW64GRljgZJFH1mNr2BZHWcnFSW1+vd+Wmz+63VHrdFcp4RvdSN5eaVfXsF6ljb25iuY1bModWO5iWOThRz711dbwlzK55mIoOhUdNu+33NXX4MQsqkAkAngZPWgkKpZiAAMkntXm97qkz63Al3eMyWc09wVOwmJtzJEMHBJKk+vJ4FbF3d6tc+GbGz1DEd1ehEvZYyEESOPmVSf4sd8dAfaqMDoJ9c023sBfSXSeQ2dhHJfBx8o6n8KvedH5HnFgse3eWbgAYzk15paEwa/DHDfNGbwotvcyMCVt0zwM/c3EnCjAwR6VvfEGC4vNMsbCO4mjgvLyKG48vhfKJy5Zuw2g0AdNFqVjPbG4ivIHhC7jIsgKgeuaNP1G11WyS8spfNt3J2SAcNg4yPavFrue4k8R3VvpuklrRrcsyJswsKDaoiJXK8lskAE9q9X8IW0tp4WsIpUmjIiGIZl2tEvQLjnGAB15oA3KKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigDkbjwfcXuo+bd3kTWv2uW4WIQI2wMuB99WDE9zgY4x3Jh03wrqMWnalaXEWnRJqE6LLEu2VPIAw4wIo1LMMjBXAznJxiuu86T/n2l/Nf/iqPOk/59pfzX/4qgDjR8NdFJKPpOiGJmuFJGlwBgj8xkEJ95PujsR1ya0zp+vxypOh0+aV7CO2nDSPGokUsSygKeDu6e1b/nSf8+0v5r/8VR50n/PtL+a//FUAc/pGl61bXekrerZC2sLJ7ctBM7M7YjAJUqB/Ae/er13pU8/izS9VVoxBaWl1A6kncWkaEqQMYx+7bPPcda0vOk/59pfzX/4qjzpP+faX81/+KoAytb0u8u5LF9ONvE0E0jyeYWXIaN1JBXndlgc1zN94M1+XTtYt7e/si2o2M1oyzKMEupAYuE38ZPUkc9K7vzpP+faX81/+Ko86T/n2l/Nf/iqAMrXPD9rqOk6jFBZ2v2q6jYeY8YyXIABJxnoBz7U3WfD0N7o99bWENra3VzbtAJvKAwrYyDjscVr+dJ/z7S/mv/xVHnSf8+0v5r/8VSaurMunN05qcd1qc6/hK3h1G2lsILa2tbeCbEUabS8zqEDHHbbu/Oq9x4SmufDGjaaWhS5tGthPKpIJSM/MFOOvJxkV1XnSf8+0v5r/APFUedJ/z7S/mv8A8VUexhqdSzDELlfNqv8Ag/5s5KHwheQeKrK9S5DWFo7OvmzF5GJQrjbtAHJPOTUOm+EdXs9Vt7ie5sJraE3m2EI2R5xyAT/EPXpjtmuz86T/AJ9pfzX/AOKo86T/AJ9pfzX/AOKqfYQ/r+vIt5piGrO21tvX8feZg+GNCvNLur+6vVsonuFhijgst3lxpGCBgsAcnca6SofOk/59pfzX/wCKo86T/n2l/Nf/AIqtIxUVZHJXrSrzdSe+n4Kxm6ppFzcXYvbCe2iuNixutzAZUdVYsvAZSCCSQffpVY+HJ7+GBdZv2uDHM0xSIbEJIKgeuACcc9Tn0rb86T/n2l/Nf/iqPOk/59pfzX/4qqMipNoWl3FqbaWxhaIuJCu3Hzjo2R3rK1/RNTvp7STTms43tARbyzNITHkYJKg4bp3/AEroPOk/59pfzX/4qjzpP+faX81/+KoA8+T4faxpT6aNG1WArb8yNdozHeT8zrg8nk4DZAya9FjQpEqM7SMAAXbGW9zjio/Ok/59pfzX/wCKo86T/n2l/Nf/AIqgCaiofOk/59pfzX/4qjzpP+faX81/+KoAmoqHzpP+faX81/8AiqPOk/59pfzX/wCKoAmoqHzpP+faX81/+Ko86T/n2l/Nf/iqAJqKh86T/n2l/Nf/AIqjzpP+faX81/8AiqAJqKh86T/n2l/Nf/iqPOk/59pfzX/4qgCaiofOk/59pfzX/wCKo86T/n2l/Nf/AIqgCaiofOk/59pfzX/4qjzpP+faX81/+KoAmoqHzpP+faX81/8AiqKAJqKo6rK0VqrIzKS4GVOOxqC2eV1+aV/xY1m6iTsBq0VgazrdvosAlvLoxKzbVGT8xPYdcmvK9S+LV1dPcRWBYRhjGTvYH2IIwVPGaPaIdj3OivnFfinrlrMu/UZHfO0xueD6D26iu+8J+PINXYW013cfbC2MMx2569fwNDmI9QorEhNxcIXhujIgOCVc9e9WN04X70n/AH1S9qh2NOiuU1K+uI2k2XEqhVxw5HNM+ImoyaZ4egniu5LVjdKu9JChI2scZB9v0ojVUr26D5dbHXUV4Qvii+kO5dbvuO32lj/I1J/wkepluNYv+ewnk/xo9o+xp7F9z3OivCf+Eh1bAUavqOR1PnSVIfE2p5A/tPUjjuJZDR7R9g9i+57lRXhr+ItWdSE1PU8+0ktZdzrfiZ7qPytU1YRg8/6RIB/OtE7iqU1DZ3PoaivFU1vV/LA/tS93Y/5+Hz/Opf7c1UKD/ad4f+27/wCNMyPZaK4H4uahe6b4UtZrC8uLWVr5FLwSsjFdkhxkHpwPyrxxfFPiP/oP6r/4GSf413YfAyrQ507HNVxKpy5Wj6hor5iXxR4i/wCg9qn/AIGSf41KvifxCf8AmPap/wCBkn+Nb/2VP+ZGX16PY+mKK+bU8R+IT/zHdT/8C5P8apa9r/if+zvNt/EGsIUYE+XeSA498HpWVXL504uV7lwxkZSSsfT9FfJOk+OPEn2uNZfEeqOd4ID3kpDDpj73vn6gV6UNU1pCM6tflWAZSLl8EEZBHPf/AArnoUPa7M0q1vZ9LntlFeOJq2rY51S+/wDAh/8AGux+Jd9dWHhy3ls7qa3kN2ql4ZChI2PxkduBTq4d05JX3FDEKUXK2x2VFfPB8S65/wBBrUf/AAKf/Gs/V/Fuu21qso1zU1wwB23cn+NZzouKuEMQpNKx9L0V8fy+OPFlzJlfEOrIOcKl7IOPf5vakh8U+MZCMeJdYAPrqEv/AMVXPzpbndGjKWx9g0V8mJ4i8TggP4r1cN6fb5f57q0bXxH4hYlf+Em1cuqlsG9kIOOf71S6sUbRwc2fUVFfNk2sa2tss/8AwmF95jA4hF5OWA5GePl7Z61ai1nXrQFT4j1C5VvmSVb2R1YdOpP+FXSnGo7JmNehOjHmaPomiiiqMTN1p9lrETz+9H8jVaKQLEWyQAMnjOKsa2pa0iAGf3o/kaybyRItKuHmICBSDvOAe3NcddtSbLirtI4fxbql1qim1vLdk0+SQNDypZMf3uDgNzgenfqBzUun2VtZOufLWQsm/cCUByBk5Oeefxpuq6jLHcJbWYaWWRvkVOh9ST2Hrmpp7d201ZLtGmc5Z3VTtJyOOoA+73Ppz1B89Ocne52uEIow9I0DT7h7trkNKomKowz8pX/IH4VD/Yd7p0r3ySG1Ai8z7PCSEjQEhVOOW3ce5znvWzBAsks0sBKI33YwuC2AuWI4wWHzeo57jm7Gtvqlt++JktiR5rMxUv2GNp6deT7dMDOqqyjqzFxi9j1TwHfLe+FrXZGUSFfKVSOcDoT9Rg10MyEqQpAJ6ZFcj8P1gtrOa1tJLiSANlBJKrqo4+7zuHGOG/DNdoR1ruXvRuc+zOUu9PkaV90W4McnnrVb4o7f+EatdxABvV6/7j11ktskg+YKfqK5H4qAN4ZtAf8An+T8PkeqoQ5WwbPJgQDhyCc8gdqVZ1b7oPY9DwDj0+tMlGZB+6GT3B6mljdwSREq47HjjpXQ7DRY819pk4Vf9oEd8elSW96SxVQXHqOMdcHvxx3/ACqrJLKUBSVBznG7pxUiZW4LG5RcgDP51Oo2W1uncBkkXoOM56/hUqeeTlm4PJxjgflWe08J/ePIG2gAkk5OPpQbkKqszhUY424IH59qEyWi+32pRuySOcgY/wAKfaO5VlOcjHU//WrPMqM2zzUGeenQe3rWlaAJC4WQOTyTjB9se1UI7T4zDPg+0/6/0/8ARcleIKte5fGJd3hG0H/T+n/ouSvFUjr6DLf4HzZ5GM/ijUSrEceSOKfHDkjirsMGe1dzdjlGwwe1XktVkQq65UjBFSwW/Tir0UQA6VzzmrWKSPNdZ8NXGn3zSQKxhblWHQV1PgzWGuHGmXxJlc4hkP8Ae/uk+/PPrXTyRwtGsM+wrMwjVWONzHoB71zF3pH2K8cSIyvG345HQj+deJVj7GfNA9OlJ1I2Z2IjKnBGCDgg9q6v4tME8K2pJx/pqf8AoD1zVvc2+qwQXFpIJHf5ZFYYYOMZJxgc8frW98ZDjwhaf9f6f+i5KdWam4smEOWMkzx17lR0NZ97OJYJEcAqwwc0jGqs43RsvqKJ7MmnFKSIIoY44/kQO4GXI9f/AK39ahS5iSWMOrLFkltnUg1d0vT5ZR5rXKwRg8E8n3qzcWWkwSFYBJcnI+djxnv6fyrx6klzan0tC8kvZxuZYyVMkatsz1IrS0u1mupQsUbO3YqDnP0FOuYIUnBjR4IGX5YwcA+/b+VauhX5sNTtZYCUKSA5KgjsM479aym/5T0adGta9hP7M1i0WC5NlOquDGGaMg9eT7YyKlilibzNsbwtkYiP8Ix/+qujm1C61azEF7JhFkdSXRV2swGP1Wqk1hbNYvNatwn3RkZ25PXFVhk1UTkYYuhWdCSZ9DUUUV3Hz5Q1aQx2qMEZzv6D6GuM8dySnw8FiBHzDcinDOPTNdrqjbbZTjPzf0NedeL72VbmGOMcLzleuenHU+h45rz8bJpWR0UFqcpEfs2i3LWohguncqjyJuQDAILEAHAJGTzwDwailW9Ok21ldTZuHZlmVgOGErquCGII2qW4479xW1BbRTaNeG8DBI5FaGI4LMCNvzYxjPXaOgxnOc1Vl2rITcxsCwd93TLYOO2QOQRk965oO6SNKj1uVLzV7W0tbS1mRYpJSwRYxl8biA20c7d3HXrg1V062+w6hMWk3Wd6hYruwQzLzx6Hr+lSWkUzrPOrq0cmRO6nAIUkKD7Dnj3+tR2+bi/jaQ4jXAyeAB2rWaVrGcG3qep/DzRb7SdDQX0paWQBuvXPOfc9Of8A9Z7H1qK1QR2sSAYCoBge1S5wK7Yq0UjF7iZrhPi9IY/CdqR1+3IP/Icld0CvpWD41msINGifUZZ44ftAAMPXdtbr7dauPUR88SXs0gAB6fhzUJe43DEWcdCEJz+VekPr+hW8J8u5vZWzwBIE4z3OaiPiXQzbxNLDqDSFQxRbtgFJ6jO4ZpXkNSRwMZ1Bf+WEjHHTyTzTmfU95ItZw5HQRt/Su5TxB4blLNLb36MRgFrxjnnof3lEd94NcfvYb5VPXZeOOx54k9eP88v3ti001c41RrZhCmxuXRmOVMDE/n26mpCuqNGClnd7x95RA5ArbWPS7qdktrfUnUHgDUGHb08yp20e2lgdoY7qFFyWkk1Bjs4z0+bP5+tElZXudLw8VG/Mjn4k1did1ld475genyXl/a2rboXgGNokmBUL+Y/SuotPDVlJZQTiSd1mXzPmkJ69O/8Anmqmp+EIZLctbPiRfmAdQ4P1BBrH21nZnM4HffF1d3hS1H/T8n/oElePRwZ7V7P8U03+GbUf9Pqf+gPXlkNv7V9Rl7tQ+Z4mM/ikMNv04rQit8dqmit8DpVuOLHat5TMEhkcWB0qykdNd4oInllcJGoyzHsK5fVPFzM/k6apGTjzD3+lcdWvGJvTpOR0184hspHMhiZBuVh1DDkfrUdt4oik2m7Me5R8xcgZJ788etcGb67upvndncn1JrrdD8PfaIhPqVsBGFBQNncx9cCvOqN1JXR20l7NanTrfXTeQ0C+aqAloY12HOcgqGIAGARg469eDnV+M5x4PtP+v9P/AEXJWLeabbX9m1pPGDERjC9V7Aj09K2fjSceDrT/ALCCf+i5KTpuE0V7SM4O254Wx4qCQ8GpSeKhfoa3exgnZl6ys1nhbDDzgw2xuQFOffI/mKskW6zvuwEEYzlRu3YzyCRk7mxjpgHris2BxjMhZY/vNjnAHfFKZ91jcPApAeJgC7bduCO+ec4IHXJ7YNeVUjeR9bQqqFJXfTYsO5unjO/auVXrwMsF4/E4x71ZFokHzSMz7UMrJvwwUZyQcEchSRn0NJp1vcXxuILO3JnXbiQZjzHlcsM7gDyec5G0cA1pJMYSkWBJLHboLkhiWLqwZd29B0wQDnJ4545zUUtzarjZKSjSWljcitHu0v4bCOSVhJ5gjVfmZd7AHHYfXn2AwTQg0+XCb3jXfn5c5PH04/Wr+m3pt4BGQ6RJaqq7CFZdpXL9Qc/KRnin299/bKz2935pu9/mQyhDvkIAyhAPzccjPTkUk1e6Lo4qsqTpzej8j3uiiiuw+XKGrMFtFyergdcZ4NeTeP7qSz1TTokMZMwIVWY7i25eSPQAHn6V61qrbbZDz/rB0+hrzH4kabLJpttqyoJPsLqyxAgE88kE+2fb8q48RFNmtN2KNq1taWtxbzMNnyK9xISYwfm+9g4HY5PH8PbAyjbajcyXDaf4lgvLCEqhxsmk3Y5UuR2/vZ7jIzmub0XxPqTeJ7yCLTcW8sZZoWzkqD6nv/8Aq9auTarotujXV34fQ3DklSgDLnPBzjOB8v5+1c8YcrszSd2bd4gjhNksit5mWkEbD0xjHUHAJx6nPpUFhEmta5a6DbuuJGHmyKu4KiHJGR3IHFcXbajq3iTUhHpsItleX5QnDBmyAB3zggDHfmvcfhn4RPhXSrn7Vsa7mncMQmMKrFRyeSG27h/vVoqV3dkSlZWR6CpAAHHTp6UMyjjIqs0w6ZqJ/mOc103Mi716EVznjyKKbRLcSrCyi6Q4ltjOD8rdh0Pv/jWorMOjGsD4m6la6X4etJ7uSRIzeoo2LnJ2OcH2wDVw6lwipSSlsecXs+mx6lHbSnSLdeGmxahHibGQpXcOoPb8q07e3X7JNLd2NnbKq7j/AKCeg5JLE4HHf071iTeM/DNxIJpixdQFLmNh+mOewqa68e6BdWkkAvCjOQNxif5cHPPHTjGPejlVzrVCioyu0zRl1WyaCOK2uND4jwcwFZPwAJz9fr7Z2IJLW4CWiX+nJtwEkNgQM5PXDAAVwi+IvD2TnUogCO1u3P8A47UyeKtDQjbq/fAAicZ/8dqko3vqcLXRI2dSsdPvfE/2eSa1NtFEZPtttYuVZyfuEqXycZPX8Km+xXBVo0Ejw5I5cqGHP8Pp9aXTLn/hIbF7uynNxBG+x2EPO7APQcnrVmMSPIyC8wy9QV5H4Z4/GoquMdhxu9yhb2lxbosFuNsUfCxpIRx6AU2aC+eBmSd+OTmQ9PTFahtJAR/pByOQduKje1YKf3/bHCispVIjsdj8R08zw9bj/p7U/wDjj15zFBjtXpvjxd2hwD/p5X/0Fq4FY6+gwkrUTycVG9QjSOpAYUeJJpkhWRwgkk4UE9AT2z0HuQOpAqZUp4SrlJszirHD+MtQgkZYbfUIhbnGXRw3mcnOMZyBhh0J9Qfk3y+HvDImgiuJWzE43lioBYEAgr6jkj04yOtdbHpOnpL5yWFqsuzy94hUNtxjbnHTAAx6VfCcVyewu7yZ0+2srJFS30uxtJRJbWqxspyAOx/n+fNXQp79qcF6VIq8Vqko7ENtjVTirHxqOPBtn/2EE/8ARclMC0742f8AIm2f/YQT/wBFyVhVd5RNafwSPCN1Rueadmo2qyCSBwuCw3AdQSP68VKXwMKCAp3BQTgEc8dhyAeOOlLp1q93KUSOSRgchUwv45PQe9dCmkSWgRpZo4AeSttywAHdz938yDXmV7qVj6jB4ijGjGc91oJobSWOka2STBcNAGjJX5mAzkgHnHIGRXNPfeRcFA6O2CcgghW64rtkudA0O6QQNE1wVOZZC0hBxzjAI5BPIFVNRv8AwlqFy8s+lzXDbRmW3Xyv68n64rG0UtSamLcqrlSWjILPVZr3y4mkzM4OAMqwLE8Y4Hf0rd0KJxqNjew6ip+zTPLM0bhjsIXfuGCQRgjnqW471l6LYeFnha5e8ubaKF1CpJIJHOc8gBcj/PNXLvxUfD93c2GltALdJiS0EB+bHAJ3cN+HFZRqQ5tB1KlWa5bH0PRRRXeeOUdVZUtVdiAFcHJOMcGuE1rVotQdLS1RpWwyquMBgByR68Bvyrv7+zN7CsYk8va+7O3PYj+tZsXhuGEsY3jXfw22EDd9ea5a1OUpXRpBpbngltpsF5rFpG42NPIsCuAcqGbaOARnGcgdQcVf1DTE8NyzabLIryqu1d2CuxsHcDgZx0zgcg45Ga9Li+GUEeoQ3h1Is8U6zAGDqQwP97261v3nha11Eob1be5MeSnnW6vtJ9M9Og/Ks/Yz7F+0R5h8OLK0s9Re4VAJQmYFUcDPDMeOvH4cj0r0SbVJIQPkD4/2u1X4vD6wxJFHMqJGuxFWLAVewAzwKqv4U3sT9txn/pl/9eqdOp2ITiZ//CRruI+yuW9smlHiKMu2+N1UdO5/LrVpvB7kkjUihzkFYACP1oHhCQk79RVgT2t8E/X5v5YoVOqO8RYtZtZCF80BiM4b5T+VXPFSW76ZEtzdJboZhhnl2Ana3Gf89Kp/8IcvP+m8egix/wCzVp6/ocWv2CWkzqqrIJAWjDjOCOh+tbUlKN7kSt0ODurXwp/qdQ1LQ2yMmO5vFOfqCar/ANk/D+Qff8In2F0n9Grf/wCFaWgQgXMGSDgmzXj070+P4cWqA7riB+uP9EA/k1a80hadznP7A8CNkqPCjE8/8fY/+Kph0PwgpPlweDpRg4BvBnP47v5V1sfgG0jUL5sPU/8ALv2/FquW3g6zt+hjP/bED+tK8gsjiItL0pLZYYF8MQRCQuy210uCeMfweg/pXOubhL+eGF4ZURzh0Y7SPY4wcY7fXvXrZ8JWpuJJd8eH/h8kcfrUy+GbdANrJuHcxA/1rOpTc9xppHkhW/C5IXH+y5/wqlc6ldwR58m4f/rmrGvaf+EdTBHnjrx+7/8Ar1PFoqxReWJs++z/AOvWSwq6jczO8bjOjQ/9fC/+gtXDKlema1pX9sWaW/neTtkD7tu7PBGOo9axB4I/6iP/AJB/+yr16NaMYWbOCtSnKd0jkgtPC11f/CFf9RD/AMg//ZUv/CF/9RD/AMg//ZVp7en3I9hPscuFAFPrp/8AhDf+n/8A8g//AGVL/wAId/0//wDkH/7Kl7aHcfsZ9jmRTxXSf8Ih/wBP3/kH/wCypf8AhEf+n7/yF/8AZUvbQ7j9lPsc4KPjb/yJln/2EE/9FyV0v/CJ/wDT7/5C/wDr0njbwn/wmOiw6d9t+yeXcLP5nleZnCsuMZH97r7VlOpFyTRrCnJRaZ8w5prHg17H/wAKJ/6mP/yR/wDtlIfgRn/mZP8AyR/+2VTqxJVOXY8WLCOUN6elXbPUr12CG52IcZPlqeK9ZPwEU5z4kzxx/oPT/wAiVPa/AqO3lVm18SKOqmyxn/yJXFW953R6GHcIwtPc8Yl82e5l23Esg5IO4jj6VX8pnfD/ADEDqxr24fApVIMfiLaw7/Ys8f8Afyo3+AqmbzE8Rlc9QbLOT9fMrldOd9j1KWJw0ev4M800COOSaeBtuWiBRTyCwIP8gT+Famr2v2gxXzlB5sKq4jBAUqAhHX/ZB/GvQLX4JNayB08RnO3bxZYyCCD/AMtO4NXpPhEWhEA10iEEkI1rkAkDJ+/7Co9jVN1jMMpcyl+D/wAj02iiiu8+eK18WWFSrlfm6g47GqJuCAf37H/gRqfWJDFYGQbjtOSq9W4PFYum3sGp2EFzEhCuPmU5OD05P4UNpblKLauTzXNwrhY53Y/7xqC01W5ZvvuxBIwW644rCsvELza3fWp2JBl4YOMtvQ4Jznv8x9sCqtzLaaKhvr/UFihh5JY7c46D8a+fzT6xiuSOGb0ZvhJUpKXMdf4m8Tx+GfDraxcWs80SFVZYyAVycAkk8DOB+Irze38YeMtS1K31GS2NpZNk/Y/NCnYd2CctnOQOw4z0rk9X+KTeIfEUMd5JJaaHp8nmJF5ZLzOOAzDPBGcgdu9UrPX7/wAQNcJZM6iCPZGs8hPnHp2BIJzk4PPtyR7lGVeMY04xvK2rZmue7jTjds9W0vx3e30zpPbTWxUBwTIHjZfQSKSpPU8GoPEmqeLdaEMHheV4WHMh8zGfTB9K8VS71/w9FcAP5iEOoV4vmTAB3A8kDJ/EA+4Ptfwa1+PU/C8i3WoQ3GotO25ANpVQBhegz3Pfqa6XUlRd6sLC55QlacUdlpsOvHTrVLyaEXSoBOQ5Pzd66GuK1291/Tre4n0WSGYx4dbOeIszgEllVt4PPb0wcZBGO1rgw2NpYvmdN3s9QqQlGzfUKKKK6jMKKKKACiiigAooooAQnFG6hulNoAdmj8apTahFESFBkYf3e1c/qvi8WDhFSPze8Y+c/nkAfr9KAOuorzu18d6ndXiR+RYwIf4pi4z7ZHAP1rWj8bQKs5uIVHlAZENwrn82Cg/8ALH2FAHXUVj6f4k0rVHCWl9G0m7b5b5RicdgQCfwrWDfSgB1FN3U6gAqGe5htk3zSpGnYswANF1N9ntZZQASilsE4zj37V5DF40tNb8641CSa3uYSRLbSROzQt/cCqCc8enPXvVRVwPSJfFOnqQI/Olz3RcY/wC+sVNZ6pJey7Whkth1BYg5/wAPyrkYdOuJkDpbXADf89Ld0PtnIH8qZe61Lo7K13q9nZoDtIvmUbj6ZYg5FXyx6E6nW3es3Np5jCxMkMZwZGmUE/gBUEXiiNs+ZbSKO2xg39BXK6fra69I0VpqE+oRs2CbeF3hQ+hdFKj8Tmr2qxrodg15fRTFQwVVQKd5J7fNwAMkk9h+FCUeoanaWd9b3yFoJQ4HUdx9as15lpGoavfeIbRrG1e1sky00sgOJ128BScbgc5yBgbcZycV6WpJPOfxrOSsUOooopAZPiKf7NpZlxna449eDXmd38QtL8JQpFcGSUfNtWJOQTk9yP8AJrv/ABtbG48OSMN2IG85gpIyFUnnHb/Jrww6Np/xCuzYLJJDdWDN511EvmRNGfunOQAxPG32zxg45cRhacmsRUm0odOh0UJ6OFr3OAg8VanaTrcw3su55WkZNwGMn29j/Oq91rNzf+TFc3Mrxrl3Z2Jy+OnJ+n516J4q+G3hnSfKurTVLmzcylvs8w3Ky5GdpwCuF3H5s9uh609fOn6laWOm3qmF1hBSbaQySHrkE8jAX6/hUUMzpTinRWj8jCrP2D5bHm9vHLLmTd8oIB55zg//AKq9R0v4fa9caEl7aPaRiaESeWJD5xUKMKAFIDH69xnHIrW+GnwtuLbz9Y1qGCWIgLZREh1kBz+8K46Yxtye5OOlerWNo5ugynao4ZmOOK58fmuJw9aFLCQu3u3+h6OHqQjDmvY8l05LjWPBXlwyKbjgYfABI4x0PBXC/ia85tLzUPC2uPLa+ZayK6+dbjGAuQflJz+B9D1Pfutf8MXsuraytvPex28t408TxJJLbujbmBBTdnA49s1i32ha2uuxz6iy3dlCVtxctKpxGWCqdudw5Yds19DiJxqQSk1f1Co6VW0JNWf3nqXh7x5FrEFu16RE5XDSTKUzxnnsT78Z9K9er5n+F+gDxHq9zbXsKtp2nMJHkB2uHyQEBBzhsHPX5QRwWFfTFeNhsBTwtWpKH2rfhf8AzOGopRfI3dLYKKKK7TMKKKKACiikPTigBaKozajDFIYlZ5phx5UK7iD74+79W4qxbXEdzEJI3DA56exIP5EEfgaAJW6Vl3d00zvDEcIvDMO9aNw4it5JCM7VJrmg8tvEML5mF3FAQGJwTgZ4z9aQ0Tsyx4LDC45J4ArCuPDEN5NJPbXobzGLFeG5+ua1jforYDlHLbQD8u44zx2PHPFTJqiBvnH0xQOxiw+DIgVM92Sn8QRcH881q23hjS7faTbCVl/ilOc/0rTjvoHwQBn6VMJlI+UCgCvDpltApEVtFEO4RAKtxgwKAGyvoe1MNwg+8QPeoZbnKMUBPuO5pgaX06U+qtpNJPbRySxGKRlBZCc7TirJoJM/Wri1stNmvr2dILa3UySSSDIAHtnk9gO+cV5nYPp3iNor17MCKZd1uZI1MkUbfMApOSvB/hIzzya7TxppUniXQrzQzKYIrhVzOgyVZWDKcdxlRkdxkcda8RttM+IngGZYI9LXUrBWbYyI08PGCWyhV0HUYbA6nFXETPb7ewe2tRHa30sceOPMklkb9XNcN4l8EaJq2rvf6rH9uuXwGkLyLwOgxnpWZZ/GGSWACTw1K4Th3tr0Oob2Hl/+zfjWdqfxZ0kuCunakhHVWWPA/HfVLcR6R4Q8N6RpcJg0qH7GGO6TyXcM31O45/EV1j6bbj9+6l5lH+tPDY9yOTXh+lfGiO3kxbeH55v9trsRj8Rsb+ddCfGnj7xFbr/ZOlW1pBOwEU8UZuCh925UfUrSluBp+KvETeGYBqFuIfNWVFSNjgOGYbhwQT8pY57YJ6A132jalDrGk2uoW+fJuIxIoPbPb6g5H4V4/p3wl1/XtRGo+L9VkVMZaJZPMlI3MdgPKxr3AG7gnhTXslhaQWNrDbWqbIIo1jjTJwqgAADPtUyaY0i3RRRUjOc8cq8vhW5to3WN7grCHfopY4yfb3wcVR8HaFoWh6C66W9vM0x8y7uEbeZHxznrgD+7xj6kk6Xi2eKDTbdpk3objBT+98j/AMsZ/CvnbXfCF9PqAudKMN2c5JZwpXHch8DBA6fzpT+Gz2M3JqWhs/ELWtP1PxUogmtbmC2t5Q8YcFS5HQ7T7CuStNPGt6zdTLqIhuradI4iGYMMMQCGzxjGc8+tXT4SmtraMx3djbSRhm8qV2ZQSQcZCnI4I59veqVh4ThsXMp8VpDORjdYp5rDnsdyn8hXEqWr5XbsL2cqsr3O38QeK9Qs7E22pXllfxW6nIkuHSSZwR8pCbNx56gbRjk5rn4/Gv8AaVlc2tlo1xcXJRlCNMxWMnIDKpLE9hWWvhvw7bH7RdalqN1IDlyq+ST/AN9K386uWdr4einF1aWt1JMhzmac8Z46oUP6VpGhCMk6upSpqEv3iuijZ6v4ovFm04LLBKAHRNrY69R19/QdfxyJ9W1WGR4pnuVHlCQRXC4bcCDkDA6EZr03+07GKKG6gsrcSKmxwBv2gZ4IbPqfzNXI/GenO8T3CKt1GMLKoAKj2xUOrTo1fdjdEJxjU5kdH8FtPhi+GltLEx8y8mlllBbowYx/yQfrXq1eJ+GPHUFhqrDUZDPaufluyS7IOBg44xxXr2qatZaNbLc30rRws4TcI2fkgnooJ7V0wmp3kbc/NqXqKq2V/bahAs9pOk0Z7qf5+n0NSzSpEmZHCg+p6+wrQCWormeO2geaV1SNBlmboKonUJJziyiZxnHmtwo5wTj25yDjpSPp0t3t+13TZVlcJGBhSO3I5HocA8UAUn8S/aE3abbmaM8LcStsjP0zyeeMHFN+y6nqP/H1O4iJGUA8tcdCMfePQnB454JrZtrG1tZMwwqrckHqQCckDPQZ7VaxQBl2mi20ERjdRKrAbkK4Q8YxjuPrnrWlgde/rTsUUAZuuzCHTTzjewXOcY6n+lcRf+KrbSWmW9sJFjjPl71Yb3fAYD6d8/T1rtPEEIuLBIzjBlHBxg8H1rmNT02z1G3eO/jSRSwQh2OT83GWwGHJHHHf8QZUtvEWk6rG/wBgvY5WwQYJBsfHHY/XHfnvVRJY5JUkiBj2AoI1Yqo74IBxn+VZVv4dtNDjvpbR5HE0aKH+VnXnPykYwGB9z8ue9UNMunGptEzht5KsSMZwOuOPTHT+dS3rYuy5bnYWq3PmFjfT4/ugJgf+O5/Wtm1acMGa6kYD+E7cH8hWRZMe3StWJsGmSSXc32WDzkt5Jy0iKQA0gQEgFsZ5x14/TrV2GZppI44lIydpeQfP2ycdv0PHIqIEbe2T0zUlrL/xMYUVHY4L9OAMY6/jQBtqABgVJTPXNPpkjJYo5V2yRo49GUGsO1c/ZUZj/ACSfYVvHpXLz+Td2V1amTy0yVVuxUEYxyMjPB5H1q4CZbubaC9UR3VvFcIONsqBh+R6dapJ4V8OE5Ph/Sc56/Yo/wDCnafHND5qy5KhsRu7N5jD/byBz9D0xwOa1Y0PlNKd21BkhFLHjngDk/gD9Kp6EoksLCysl22lnb2646QxKn8hVuaWOGPdJIqL3ZjjFZ2m38d7b2s6LKiTpuUSrhh9cZH4gkHqDgip9SgmuLNkgZQ/cMu4MMEEYyOoNQ9Rongniu7fzIZFdG6EVOOKwLWe2trSW30wRrKZXZ4y2SGDYcBQc9iBjjit5Dnnmk1YodRRRSA434lxNL4bt9shRku1YEd8I/FeZ26z30JSMs5YkbUOSPbH+c16r4/hln8NlYfM3+YSPLj3t/q36D+ftkDBII8psbTUdF1Br1Uu1YWwc2xDuJDuwWdgpAIznCjd97jH3oe5SWhyWofaIJrq2lQKyAgqcg5+lc5HG8cwnQ4ZTwT1HevTdR0eG91b7XFMkckif6sqzFjnnjHuOfzx3zYvCatF5f205J5CJ0xxzuKjt61ilNTutjKMpKWhzc2u3upacbNxHDbFiWEald/HfPPb6VnxwPGcRsVwOx4rrBomnLerbmVmBYJuBBXcfXBJ6g9CaszaDZx3iWrxpM7MBhXOBuI55UE43Dv3rZy5tGypSlI5EXrIvlm4BKHOAuf16VLAPPPzuwOM7SP51qat4ftUuI5YLiURzxKwgNvsxlc/fDk5rpdG0SwvtOjcCSOZQoyyoxYk4x90e1ZuCXUh05HDpYyGV3RfvAZLNgH8q+p9dt0ubBY3AI8wHn6GvnbUrlbbV5NPt4kEaJGVl3PuOVB5+bHf07V9Jagkj26iKJpG3jgY4GDzyRV00uhUYuO5zVhYHT5jJaExueCVGc/h3rct9OWVfNvP3rtk7WOQAR0I7jnp0oispyQGKovU85bNaSqFAAHAGBWhQKMY+nFOxRRQAUUUUAFFFFAGbrhddP3ojOEcMwXqBg1yz3ryEBZVJUY6Zzz+Y7//AF67pulY+oeH7O+y6ZglP8UY4P1H+TSHc4PW4EuLdtgYtuzgyhccEcd+/wBayLG08m5eaQqZXySVBAySSev1/Wuq1Hwxq6Ei32XI6ZjYAj6hjx+Ga5eVpdPnRbyJ7Utkqs0bJux1Iz/SlbW4XOmsBxWmmMmsLSrp7lxFaRNcu3aNSVH1PYfiK6a10W9lYPcyLAvdVIZvoew+vNOw7jUl6LyWPAA5JrX020khLyTqFdugB5A96ms7C3sx+6Q7iMF25Y/j+FWqYmFPplPoEIa5NoQs7wSZKpIwKdiueM/nu/EeldYelY2sWbj/AEqCNnbP7xFGSeOoHftVQdnqBViYbwq52KAFySTj6nrWtakC2fPHzY647CsU+bbSEzxOnOM8YORnr/hU8t7ZyWht5UklDHOERmH48cj26HoeKueq0IjuXLVfItLQMJtyYQid98gJOPmPc+/etHHyiuetmtkUG2jESh0Z9wCZCnPCgbc+/wCfStkTvKo8uJ+ecn6/l+tZpWKZHdW0UhMvKuF2qVcjHpxV2NQqADsAM1BHHI0xMuzYB8uOpPr7VaobBXCiiikMqX9kb4W6+aY1jl3sBn5xtYYyCMckHPtVG48PQzLhHCHcWJKbicjpya2aKVkO72ONuvAKXLlhqAQmMJ/qM9Cxz97/AGv0qGL4d+VZrbjVM7c/N9n7ZJ/ve9dxRS5UF2eYr8IFW6M39t/8tfNVfsnQ7s/3/r+dW5fhe0upLef21jCBdn2XqQQc53+wr0OijkiF2edXvwrF5JCw1gIIxtA+y5yMtx9/0IH4Vb0v4cLp1rBCdU83yixz9n25y6sP4j024/Gu6oo5Ij5meW6l8G1v9TW9TXPKIjSMr9k3Z2987xXqVFFNRS2E3cKKKKYgooooAKKKKACiiigAIzSYpaKAG7ar3mm2eoQiK8tYbiMHIWVAwB9RnoeTzVqigCpZaZZ6bCIbO3jgj64RcZNWSvHB/SnUUARqjBmLOCCeBjpT9vvS0UAJt96WiigAoxRRQAU1oo3+8it9RmnUUAIEVRgKAPQCloooAKKKKACiiigDAJAbAJEbG+kNExooHYEOH78A/9kKCg=="
    imageByte = Base64.convertToBytes(base64_str)
    print(imageByte)
