from ice.recipe import recipe


async def say_hello():
    return "Hello world!"

async def say_aloha():
    return "Aloha world!"

async def my_main():
    hello = await say_hello()
    aloha = await say_aloha()
    return hello + " " + aloha


recipe.main(my_main)