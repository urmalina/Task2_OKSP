# paint_service.py

from user_input import UserInput
from price_calculator import PriceCalculator


class PaintService:
    """Класс, который объединяет ввод, расчет и вывод результата."""

    def init(self):
        self.user_input = UserInput()
        self.calculator = PriceCalculator()

    def run(self):
        """Запуск сервиса."""
        part, color = self.user_input.get_part_and_color()
        price = self.calculator.calculate_price(part, color)
        print(
            f"Стоимость покраски '{part}' в цвет '{color}' составляет {price:.2f} рублей."
        )


if name == "main":
    service = PaintService()
    service.run()
