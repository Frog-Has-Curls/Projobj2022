import Fluent
import Vapor

struct GrupaaController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let grupaa = routes.grouped("grupaa")
        grupaa.get(use: index)
        grupaa.post(use: create)
        grupaa.group(":grupaaID") { grupaa in
            grupaa.delete(use: delete)
        }
    }

    func index(req: Request) throws -> EventLoopFuture<[Grupaa]> {
        return Grupaa.query(on: req.db).all()
    }

    func create(req: Request) throws -> EventLoopFuture<Grupaa> {
        let grupaa = try req.content.decode(Grupaa.self)
        return grupaa.save(on: req.db).map { grupaa }
    }

    func delete(req: Request) throws -> EventLoopFuture<HTTPStatus> {
        return Grupaa.find(req.parameters.get("grupaaID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { $0.delete(on: req.db) }
            .transform(to: .ok)
    }
}