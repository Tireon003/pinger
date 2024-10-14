from aiogram import Router, types, F
from aiogram.filters.command import Command

from client.api import UserApi
from config import settings

from client.exceptions import ApiServerErrorException


router = Router()


@router.message(Command('start'))
async def init_bot(message: types.Message):

    user_id = message.from_user.id
    chat_id = message.chat.id
    service = UserApi(domain=settings.api_domain)

    try:
        user_exists = await service.check_user_exists(user_id)
    except ApiServerErrorException:
        return await message.answer(
            text=(
                "В процессе проверки пользователя в базе данных произошла ошибка.\n"
                "Повторите снова, прежде чем начать работу с ботом."
            ),
            reply_markup=types.ReplyKeyboardRemove()
        )

    if not user_exists:
        await service.create_user(
            user_id=user_id,
            chat_id=chat_id,
        )
    await message.answer(
        text=(
            f"Данный бот предназначен для проверка доступности интернет-ресурсов из разных стран.\n"
            f"\n"
            f"Для получения статуса ресурсов отправьте команду /status\n"
            f"Для доабвения или удаления ресурса воспользуйтесь клавиатурой под сообщением со статусом."
        ),
        reply_markup=types.ReplyKeyboardRemove()
    )
