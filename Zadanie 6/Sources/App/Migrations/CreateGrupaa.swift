import Fluent

struct CreateGrupaa: Migration {
    func prepare(on database: Database) -> EventLoopFuture<Void> {
        return database.schema("grupaa")
            .id()
            .field("grupa", .string, .required)
            .field("opis", .string, .required)
            .field("liczba", .int, .required)
            .field("orkiestra_id", .uuid, .required)
            .foreignKey("orkiestra_id", references: Orkiestra.schema, .id, onDelete: .cascade, onUpdate: .noAction)
            .create()
        
    }

    func revert(on database: Database) -> EventLoopFuture<Void> {
        return database.schema("grupaa").delete()
    }
}