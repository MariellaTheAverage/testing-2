# Шифр Цезаря

## Функция encrypt()

### **test_one_word**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: исходный текст - `"hello"`, ключ - `3` \
_Ожидаемый результат_: шифротекст - `"khoor"`

## Функция get_key()

### **test_get_consistent_shift**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: исходный текст - `"helloworld"`, шифротекст - `"mjqqtbtwqi"` \
_Ожидаемый результат_: ключ - `5`

### **test_mismatched_text_length**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: исходный текст - `"sometext"`, шифротекст - `"textofadifferentlength"` \
_Ожидаемый результат_: ошибка `MismatchedTextsError`, контекст ошибки - `"8"` и `"22"`

### **test_inconsistent_shift**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: исходный текст - `"sometext"`, шифротекст - `"moretext"` \
_Ожидаемый результат_: ошибка `InconsistentShiftError`

## Консольный интерфейс

### **test_uppercase**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: 

```
1\n
HelloWorld\n
5\n
```

_Ожидаемый результат_: шифротекст - `"mjqqtbtwqi"`

### **test_uppercase_and_punctuation**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: 

```
1\n
Hello, Amazing World!!\n
6\n
```

_Ожидаемый результат_: шифротекст - `"nkrru, gsgfotm cuxrj!!"`

### **test_neg_shift**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_:

```
1\n
HelloWorld\n
-1\n
```

_Ожидаемый результат_: ошибка `InvalidShiftError`, контекст ошибки - `"out of range"`

### **test_large_shift**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
1\n
HelloWorld\n
100\n
```

_Ожидаемый результат_: ошибка `InvalidShiftError`, контекст ошибки - `"out of range"`

### **test_not_int_opcode**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
a\n
```

_Ожидаемый результат_: ошибка `InvalidOperationError`, контекст ошибки - `"not an int"`

### **test_nonexistent_opcode**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
4\n
```

_Ожидаемый результат_: ошибка `InvalidOperationError`, контекст ошибки - `"unsupported code"`

# Шифр Виженера

## Функция encrypt()

### **test_regular_encrypt**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: исходный текст - `"whenlifegivesyoulemonsdontmakelemonade"`, ключ - `"lemons"` \
_Ожидаемый результат_: шифротекст - `"hlqbyaqiswiwdcaiywxszgqgyxyoxwwiycasoi"`

### **test_huge_key**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: исходный текст - `"lifegiveslemons"`, ключ - `"whenlifegivesyoulemonsdontmakelemonade"` \
_Ожидаемый результат_: шифротекст - `"hpjrrqaiytzqglg"`

### **test_nonalphabetic_plaintext**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: исходный текст - `"make life rue the day it thought it could give cave johnson lemons!"`, ключ - `"lemons"` \
_Ожидаемый результат_: ошибка `SymbolError`, контекст ошибки - `"non-alphabet symbol"`

## Функция decrypt()

### **test_regular_decrypt**
_Предусловие_: отсутствует \
_Тип теста_: позитивный \
_Входные данные_: исходный текст - `"hlqbyaqiswiwdcaiywxszgqgyxyoxwwiycasoi"`, ключ - `"lemons"` \
_Ожидаемый результат_: шифротекст - `"whenlifegivesyoulemonsdontmakelemonade"`

### **test_nonalphabetic_ciphertext**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: исходный текст - `"make life rue the day it thought it could give cave johnson lemons!"`, ключ - `"lemons"` \
_Ожидаемый результат_: ошибка `SymbolError`, контекст ошибки - `"non-alphabet symbol"`

## Консольный интерфейс

### **test_empty_key**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
makelifetakethelemonsback\n
\n
\n
```

_Ожидаемый результат_: ошибка `EmptyKeyError`

### **test_nonalphabetic_key**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
makelifetakethelemonsback\n
portal3\n
```

_Ожидаемый результат_: ошибка `SymbolError`, контекст ошибки - `"non-alphabet symbol"`

### **test_not_int_opcode**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
idontwantyourdamnlemons\n
portal\n
a\n
```

_Ожидаемый результат_: ошибка `InvalidOperationError`, контекст ошибки - `"not an int"`

### **test_nonexistent_opcode**
_Предусловие_: отсутствует \
_Тип теста_: негативный \
_Входные данные_: 

```
imgonnagetmyengineerstoinventacombustiblelemon\n
portal\n
4\n
```

_Ожидаемый результат_: ошибка `InvalidOperationError`, контекст ошибки - `"unsupported code"`