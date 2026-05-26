from .validaciones import validar_nombre, validar_edad, validar_email

class GestorUsuarios:
    def __init__(self):
        self.usuarios = []  # lista de diccionarios

    def registrar(self, nombre: str, edad: int, email: str) -> dict:
        """Registra un nuevo usuario después de validar datos."""
        validar_nombre(nombre)
        validar_edad(edad)
        validar_email(email)

        usuario = {
            "id": len(self.usuarios) + 1,
            "nombre": nombre.strip(),
            "edad": edad,
            "email": email.strip()
        }
        self.usuarios.append(usuario)
        return usuario

    def listar(self):
        """Retorna la lista completa de usuarios."""
        return self.usuarios

    def buscar(self, termino: str):
        """Busca usuarios por nombre o email (coincidencia parcial)."""
        termino = termino.lower()
        resultados = [
            u for u in self.usuarios
            if termino in u["nombre"].lower() or termino in u["email"].lower()
        ]
        return resultados