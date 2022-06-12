import Fluent
import Vapor

func routes(_ app: Application) throws {
    app.get { req in
        return req.view.render("index", ["title": "Hemlo"])
    }

    app.get("hello") { req -> String in
        return "It works!"
    }

    try app.register(collection: MuzykController())
    try app.register(collection: GrupaaController())
    try app.register(collection: OrkiestraController())
}



