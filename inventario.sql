BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "administrador" (
	"idUsuario"	INTEGER,
	"departamento"	TEXT NOT NULL,
	PRIMARY KEY("idUsuario"),
	CONSTRAINT "fk_usuario_administrador" FOREIGN KEY("idUsuario") REFERENCES "usuario"("idUsuario")
);
CREATE TABLE IF NOT EXISTS "empleado" (
	"idUsuario"	INTEGER NOT NULL,
	"turno"	TEXT CHECK(turno IN ("Matutino", "Vespertino", "Nocturno")),
	PRIMARY KEY("idUsuario"),
	CONSTRAINT "fk_usuario_empleado" FOREIGN KEY("idUsuario") REFERENCES "usuario"("idUsuario")
);
CREATE TABLE IF NOT EXISTS "inventario" (
	"idInventario"	INTEGER NOT NULL,
	"nombreInventario"	TEXT NOT NULL,
	"ubicacion"	TEXT NOT NULL,
	PRIMARY KEY("idInventario" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "movimientoInventario" (
	"idMovimiento"	INTEGER NOT NULL,
	"idUsuario"	INTEGER,
	"idProducto"	INTEGER,
	"tipoMovimiento"	TEXT NOT NULL DEFAULT 'Entrada' CHECK("tipoMovimiento" IN ("Entrada", "Salida")),
	"fechaMovimiento"	TEXT NOT NULL DEFAULT '2025-01-01',
	"cantidad"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("idMovimiento" AUTOINCREMENT),
	CONSTRAINT "fk_movimiento_producto" FOREIGN KEY("idProducto") REFERENCES "producto"("idProducto"),
	CONSTRAINT "fk_movimiento_usuario" FOREIGN KEY("idUsuario") REFERENCES "usuario"("idUsuario")
);
CREATE TABLE IF NOT EXISTS "producto" (
	"idProducto"	INTEGER NOT NULL,
	"nombreProducto"	TEXT NOT NULL,
	"descripcion"	TEXT NOT NULL,
	"precioUnitario"	REAL NOT NULL,
	"stockActual"	INTEGER NOT NULL,
	"stockMinimo"	INTEGER NOT NULL,
	PRIMARY KEY("idProducto" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "reporteInventario" (
	"idReporte"	INTEGER NOT NULL,
	"idUsuario"	INTEGER NOT NULL,
	"fechaGeneracion"	TEXT NOT NULL,
	"tipoReporte"	TEXT NOT NULL CHECK(tipoReporte IN ("Basico", "Detallado", "Historico")),
	"contenido"	TEXT NOT NULL,
	PRIMARY KEY("idReporte" AUTOINCREMENT),
	CONSTRAINT "fk_usuario_reporte" FOREIGN KEY("idUsuario") REFERENCES "usuario"("idUsuario")
);
CREATE TABLE IF NOT EXISTS "usuario" (
	"idUsuario"	INTEGER,
	"nonmbreUsuario"	TEXT,
	"contrasena"	TEXT,
	"rol"	TEXT DEFAULT Empleado CHECK("rol" IN ("Administrador", "Empleado")),
	PRIMARY KEY("idUsuario" AUTOINCREMENT)
);
COMMIT;
