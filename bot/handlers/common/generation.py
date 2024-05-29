from io import BytesIO

from aiogram.types import BufferedInputFile, CallbackQuery
from aiogram import Router, F

from generation_api.txt2img import txt2img_generate

from bot.models import PromptVariable, User

router = Router()


@router.callback_query(F.data.startswith('generation'))
async def generation(callback: CallbackQuery, user: User):
    await callback.message.edit_text('Starting generation...')

    data = callback.data.split(':')
    prompt_variable = await PromptVariable.objects.aget(id=data[1])

    prompt_variables_dict = {
        "prompt": prompt_variable.prompt,
        'batch_size': prompt_variable.batch_size,
        'width': prompt_variable.width,
        'height': prompt_variable.height,
        'enable_hr': prompt_variable.enable_hr,
        'hr_checkpoint_name': prompt_variable.hr_checkpoint_name
    }

    images = await txt2img_generate(prompt_variables_dict)

    for i in range(len(images)):
        img = images[i]
        file_name = f"{i + 1}-image.png"
        img_bytes = BytesIO()
        img.save(img_bytes, "PNG")
        file = BufferedInputFile(img_bytes.getvalue(), file_name)

        await callback.message.answer_document(file)
