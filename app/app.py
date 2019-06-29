# -*- encoding: utf-8 -*-

from . import app, db, ma, Migrate


def create_app(config_file):
    app.config.from_pyfile(config_file)
    Migrate(app, db)

    from .employee.view import employee
    from .services.view import service
    from .movement.view import movement
    from .Expense.view import expense

    app.register_blueprint(employee)
    app.register_blueprint(service)
    app.register_blueprint(movement)
    app.register_blueprint(expense)

    return app
