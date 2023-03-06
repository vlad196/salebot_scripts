import re, numpy, json

def handle(params):    
    data = json.loads(params)
    js_data = data["strg"] 
    reg_pr = re.findall(r"(([А-Яа-я]+)(\s\d\d\d?)?)",js_data)
    numpy_reg = numpy.array(reg_pr)  
    Pr_mass = list(numpy_reg[:,0])
    return Pr_mass

print(handle('{"strg": "5-Альпино 100_6-Вестервальд 100_7-Вестервальд 120_11-Геометрия_22-Фридланд 100_23-Фридланд 120_24-Фридланд 140_26-Горизонт 100_27-Горизонт 120_29-Мальборк 120_30-Мальборк 130_32-Зальцбург_"}'))