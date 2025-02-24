# price_calculator.py

class PriceCalculator:
    """Класс для расчета стоимости покраски."""

    BASE_PRICE = 12000

    COLOR_COEFFICIENTS = {
        "белый": 1,
        "синий": 1,
        "желтый": 1.1,
        "красный": 1,
        "перламутровый": 1.2,
        "серый металлик": 1.3,
    }

    PART_COEFFICIENTS = {
        "капот": 1,
        "передняя дверь": 1.2,
        "задняя дверь": 1.1,
        "передний бампер": 1,
        "задний бампер": 1,
        "крыша": 1.1,
    }

    def calculate_price(self, part, color):
        """Рассчитывает стоимость покраски."""
        part_coeff = self.PART_COEFFICIENTS.get(part, 1)  # Если детали нет в списке, коэффициент = 1
        color_coeff = self.COLOR_COEFFICIENTS.get(color, 1)  # Если цвета нет в списке, коэффициент = 1

        final_price = self.BASE_PRICE * part_coeff * color_coeff
        return final_price