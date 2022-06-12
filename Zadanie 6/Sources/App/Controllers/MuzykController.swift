import Fluent
import Vapor

struct MuzykController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let muzyk = routes.grouped("muzyk")
        muzyk.get(use: index)
        muzyk.post(use: create)
        muzyk.group(":muzykID") { muzyk in
            muzyk.delete(use: delete)
        }
    }

    func index(req: Request) throws -> EventLoopFuture<[Muzyk]> {
        return Muzyk.query(on: req.db).all()
    }

    func create(req: Request) throws -> EventLoopFuture<Muzyk> {
        let muzyk = try req.content.decode(Muzyk.self)
        return muzyk.save(on: req.db).map { muzyk }
    }

    func delete(req: Request) throws -> EventLoopFuture<HTTPStatus> {
        return Muzyk.find(req.parameters.get("muzykID"), on: req.db)
            .unwrap(or: Abort(.notFound))
            .flatMap { $0.delete(on: req.db) }
            .transform(to: .ok)
    }
}