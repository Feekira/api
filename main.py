from fastapi import FastAPI, Depends, status, HTTPException, Response
from database.connection import engine, Base, connect_db
from sqlalchemy.orm import Session
from schema.schemas import DeviceRequest, ScheduleRequest, UserRequest, GpioRequest
from repository.api import DeviceRepository, ScheduleRepository, UserRepository, GpioRepository
from models.models import Device, Schedule, User, Gpio

Base.metadata.create_all(bind=engine)

app = FastAPI()


######  CRUD DEVICE ######
@app.post("/api/device/save", status_code=status.HTTP_201_CREATED)
def create_device(request: DeviceRequest, db: Session = Depends(connect_db)):
    save_result = DeviceRepository(db).save(Device(**request.model_dump()))
    if not save_result:
        ##caso ocorra um problema no db.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Equipamento não cadastrado"
        )
    return save_result


@app.put("/api/device/update", status_code=status.HTTP_201_CREATED)
def update_device(id:int, request: DeviceRequest, db: Session = Depends(connect_db)):
    update_result = DeviceRepository(db).find(id)
    if not update_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Equipamento não atualizado"
        )
    
    for key, value in request.model_dump().items():
        setattr(update_result, key, value)

    updated_device = DeviceRepository(db).update(update_result)
    return updated_device


@app.get("/api/get_device/{id}}", response_model=DeviceRequest, status_code=status.HTTP_200_OK)
def get_device(id:int, db: Session = Depends(connect_db)):
    get_result = DeviceRepository(db).find(id)
    if not get_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Equipamento não encontrado"
        )
    return get_result


@app.delete("/api/device/delete", response_model=None, status_code=status.HTTP_200_OK)
def delete_device(id:int, db:Session = Depends(connect_db)):
    delete_result = DeviceRepository(db).find(id)
    if not delete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Equipamento não deletado"
        )
    DeviceRepository(db).delete_by_id(id)
    return {"result": "Equipamento excluído com sucesso"}




######  CRUD SCHEDULE ######
@app.post("/api/schedule/save", status_code=status.HTTP_201_CREATED)
def create_schedule(request: ScheduleRequest, db: Session = Depends(connect_db)):
    schedule_save_result = ScheduleRepository(db).save(Schedule(**request.model_dump()))
    if not schedule_save_result:
        ##caso ocorra um problema no db.
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Programação horária não cadastrada"
        )
    return schedule_save_result

@app.put("/api/schedule/update", status_code=status.HTTP_201_CREATED)
def update_schedule(id:int ,request: ScheduleRequest, db: Session = Depends(connect_db)):
    schedule_update_result = ScheduleRepository(db).find(id)
    if not schedule_update_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Programação horária não atualizado"
        )
    

    for key, value in request.model_dump().items():
        setattr(schedule_update_result, key, value)


    updated_schedule = ScheduleRepository(db).update(schedule_update_result)
    return updated_schedule

@app.get("/api/get_schedule/{id}", response_model=ScheduleRequest)
def get_schedule(id:int, db: Session = Depends(connect_db)):
    get_schedule_result = ScheduleRepository(db).find(id)
    if not get_schedule_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Equipamento não encontrado"
        )
    return get_schedule_result


@app.delete("/api/schedule/delete/{id}", status_code=status.HTTP_200_OK)
def delete_schedule(id:int, db:Session = Depends(connect_db)):
    delete_result = ScheduleRepository(db).find(id)
    if not delete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Equipamento não deletado"
        )
    ScheduleRepository(db).delete_by_id(id)
    return {"result": "Equipamento excluído com sucesso"}



# ######  CRUD USER ######
@app.post("/api/user/save", status_code=status.HTTP_201_CREATED)
def create_user(request: UserRequest, db: Session = Depends(connect_db)):
    user_save_result = UserRepository(db).save(User(**request.model_dump()))
    if not user_save_result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="Usuario não cadastrado"
        )
    return user_save_result


@app.put("/api/user/update", status_code=status.HTTP_201_CREATED)
def update_user(id:int ,request: UserRequest, db: Session = Depends(connect_db)):
    user_update_result = UserRepository(db).find(id)
    if not user_update_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario não atualizado"
        )
    
    for key, value in request.model_dump().items():
        setattr(user_update_result, key, value)

    updated_user = UserRepository(db).update(user_update_result)
    return updated_user


@app.get("/api/get_user/{id}", response_model=UserRequest)
def get_user(id:int, db: Session = Depends(connect_db)):
    get_user_result = UserRepository(db).find(id)
    if not get_user_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Usuario não encontrado"
        )
    return get_user_result


@app.delete("/api/user/delete/{id}", status_code=status.HTTP_200_OK)
def delete_user(id:int, db:Session = Depends(connect_db)):
    delete_result = UserRepository(db).find(id)
    if not delete_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario não deletado"
        )
    UserRepository(db).delete_by_id(id)
    return {"result": "Usuario excluído com sucesso"}

# ######  CR GPIO  ######
@app.post("/api/gpio/save", status_code=status.HTTP_201_CREATED)
def create_gpio(request: GpioRequest, db: Session = Depends(connect_db)):
    gpio_save_result = GpioRepository(db).save(Gpio(**request.model_dump()))
    if not gpio_save_result:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
            detail="gpio não cadastrado"
        )
    return gpio_save_result


@app.put("/api/gpio/update", status_code=status.HTTP_201_CREATED)
def update_gpio(id:int ,request: GpioRequest, db: Session = Depends(connect_db)):
    gpio_update_result = GpioRepository(db).find(id)
    if not gpio_update_result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="gpio não atualizado"
        )
    
    for key, value in request.model_dump().items():
        setattr(gpio_update_result, key, value)

    updated_user = UserRepository(db).update(gpio_update_result)
    return updated_user