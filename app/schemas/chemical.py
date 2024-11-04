from pydantic import BaseModel


class ChemicalBase(BaseModel):
    cas: str
    koName: str
    enName: str


class ChemicalCreate(ChemicalBase):
    molecularFormula: str
    description: str
    chemicalLaw: str


class ChemicalResponse(ChemicalBase):
    class Config:
        orm_mode = True
