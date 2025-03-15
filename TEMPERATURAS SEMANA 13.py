TEMPERATURAS = [
    # PUYO
    [
        # Semana 1
        [
            ["Lunes", 15],
            ["Martes", 20],
            ["Miércoles", 21],
            ["Jueves", 26],
            ["Viernes", 17],
            ["Sábado", 22],
            ["Domingo", 16]
        ],
        # Semana 2
        [
            ["Lunes", 14],
            ["Martes", 19],
            ["Miércoles", 20],
            ["Jueves", 25],
            ["Viernes", 18],
            ["Sábado", 21],
            ["Domingo", 17]
        ],
        # Semana 3
        [
            ["Lunes", 13],
            ["Martes", 18],
            ["Miércoles", 19],
            ["Jueves", 22],
            ["Viernes", 16],
            ["Sábado", 23],
            ["Domingo", 15]
        ],
        # Semana 4
        [
            ["Lunes", 16],
            ["Martes", 21],
            ["Miércoles", 22],
            ["Jueves", 27],
            ["Viernes", 19],
            ["Sábado", 24],
            ["Domingo", 18]
        ]
    ],

    # QUITO
    [
        # Semana 1
        [
            ["Lunes", 10],
            ["Martes", 12],
            ["Miércoles", 11],
            ["Jueves", 13],
            ["Viernes", 14],
            ["Sábado", 15],
            ["Domingo", 9]
        ],
        # Semana 2
        [
            ["Lunes", 12],
            ["Martes", 13],
            ["Miércoles", 14],
            ["Jueves", 15],
            ["Viernes", 16],
            ["Sábado", 17],
            ["Domingo", 10]
        ],
        # Semana 3
        [
            ["Lunes", 13],
            ["Martes", 14],
            ["Miércoles", 15],
            ["Jueves", 16],
            ["Viernes", 17],
            ["Sábado", 18],
            ["Domingo", 11]
        ],
        # Semana 4
        [
            ["Lunes", 14],
            ["Martes", 15],
            ["Miércoles", 16],
            ["Jueves", 17],
            ["Viernes", 18],
            ["Sábado", 19],
            ["Domingo", 12]
        ]
    ],

    # TULCÁN
    [
        # Semana 1
        [
            ["Lunes", 8],
            ["Martes", 9],
            ["Miércoles", 10],
            ["Jueves", 11],
            ["Viernes", 12],
            ["Sábado", 13],
            ["Domingo", 7]
        ],
        # Semana 2
        [
            ["Lunes", 9],
            ["Martes", 10],
            ["Miércoles", 11],
            ["Jueves", 12],
            ["Viernes", 13],
            ["Sábado", 14],
            ["Domingo", 8]
        ],
        # Semana 3
        [
            ["Lunes", 10],
            ["Martes", 11],
            ["Miércoles", 12],
            ["Jueves", 13],
            ["Viernes", 14],
            ["Sábado", 15],
            ["Domingo", 9]
        ],
        # Semana 4
        [
            ["Lunes", 11],
            ["Martes", 12],
            ["Miércoles", 13],
            ["Jueves", 14],
            ["Viernes", 15],
            ["Sábado", 16],
            ["Domingo", 10]
        ]
    ],

    # MACAS
    [
        # Semana 1
        [
            ["Lunes", 20],
            ["Martes", 23],
            ["Miércoles", 21],
            ["Jueves", 22],
            ["Viernes", 24],
            ["Sábado", 25],
            ["Domingo", 19]
        ],
        # Semana 2
        [
            ["Lunes", 21],
            ["Martes", 24],
            ["Miércoles", 22],
            ["Jueves", 23],
            ["Viernes", 25],
            ["Sábado", 26],
            ["Domingo", 20]
        ],
        # Semana 3
        [
            ["Lunes", 22],
            ["Martes", 25],
            ["Miércoles", 23],
            ["Jueves", 24],
            ["Viernes", 26],
            ["Sábado", 27],
            ["Domingo", 21]
        ],
        # Semana 4
        [
            ["Lunes", 23],
            ["Martes", 26],
            ["Miércoles", 24],
            ["Jueves", 25],
            ["Viernes", 27],
            ["Sábado", 28],
            ["Domingo", 22]
        ]
    ]
]


def calcular_promedio_ciudad(temperaturas, ciudad_index):
    total_temp = 0  # Guarda la suma de temperaturas
    total_dias = 0  # Aqui Cuenta los días registrados
    
    for semana in temperaturas[ciudad_index]:  # Recorre las semanas de la ciudad
        for dia in semana:  # Recorre los días dentro de la semana
            total_temp += dia[1]  # Suma la temperatura del día
            total_dias += 1  # Suma un día al contador
    
    return total_temp / total_dias if total_dias > 0 else 0  # Evita dividir por cero

# Saca el promedio de temperatura para cada ciudad
# El índice en temperaturas representa a cada ciudad

temperatura_puyo = calcular_promedio_ciudad(TEMPERATURAS, 0)  # Puyo
temperatura_quito = calcular_promedio_ciudad(TEMPERATURAS, 1)  # Quito
temperatura_tulcan = calcular_promedio_ciudad(TEMPERATURAS, 2)  # Tulcán
temperatura_macas = calcular_promedio_ciudad(TEMPERATURAS, 3)  # Macas

# Aqui ya se Muestra los resultados con dos decimales
print(f"Temperatura promedio en Puyo: {temperatura_puyo:.2f}°C")
print(f"Temperatura promedio en Quito: {temperatura_quito:.2f}°C")
print(f"Temperatura promedio en Tulcán: {temperatura_tulcan:.2f}°C")
print(f"Temperatura promedio en Macas: {temperatura_macas:.2f}°C")
