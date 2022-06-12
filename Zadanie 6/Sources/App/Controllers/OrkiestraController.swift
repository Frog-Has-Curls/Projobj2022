import Fluent
import Vapor

struct OrkiestraController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let orkiestra = routes.grouped("orkiestra")
        orkiestra.get(use: index)
        orkiestra.post(use: create)
        orkiestra.group(":orkiestraID") { orkiestra in
            orkiestra.delete(use: delete)
        }
    }

    func index(req: Request) throws -> EventLoopFuture<[Orkiestra]> {
        return Orkiestra.query(on: req.db).all()
    }

    func create(req: Request) throws -> EventLoopFuture<Orkiestra> {
        let orkiestra = try req.content.decode(Orkiestra.self)
        return orkiestra.save(on: req.db).map { orkiestra }
    }

    func delete(req: Request) throws -> EventLoopFuture<HTTPStatus> {
        return Orkiestra.find(req.parameters.get("orkiestraID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { $0.delete(on: req.db) }
            .transform(to: .ok)
    }
}