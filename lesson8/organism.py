#organism program

organism = [1, 2, [4, 5], 'eyes']   # Коварный список, который нужно дописать "сам-в-себя"
organism = organism + organism      # принимаем простейший метод по осуществлению его "коварного плана"
print('organism = ', organism)      # вывод на дисплей