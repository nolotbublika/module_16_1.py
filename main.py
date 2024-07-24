from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_mane_page() -> dict:
    return {"message":" Главная страница"}


@app.get("/user/admin")
async def get_admin_page() -> dict:
    return {"message": " Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def get_user_numbers(user_id: int) -> dict:
    return {"massage": f" Вы вошли как пользователь № {user_id}"}


@app.get("/user")
async def get_user_info(username:  str, age: int) -> dict:
    return {"User": username, "Age": age}
