def pass_rate(passed, total): #Процент успешных тестов, округлённый до 2 знаков	(45, 50) → 90.0; (1, 3) → 33.33
    success = passed * 100 / total
    success = round(success, 2)
    return success

#(failed, broken)	#True, только если нет ни упавших, ни сломанных	(0, 0) → True; (1, 0) → False; (0, 2) → False
#format_duration(seconds)	#Целые секунды → строка «N мин M сек»	125 → "2 мин 5 сек"; 59 → "0 мин 59 сек"
#is_within_tolerance(actual, expected, tolerance)	#True, если actual отличается от expected не больше чем на tolerance	(10.2, 10.0, 0.5) → True; (9.4, 10.0, 0.5) → False