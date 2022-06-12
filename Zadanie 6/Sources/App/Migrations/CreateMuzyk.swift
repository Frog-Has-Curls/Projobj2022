import Fluent

struct CreateMuzyk: Migration {
    func prepare(on database: Database) -> EventLoopFuture<Void> {
        return database.schema("muzyk")
            .id()
            .field("instrument", .string, .required)
            .field("opis", .string, .required)
            .field("liczba", .int, .required)
            .field("grupaa_id", .uuid, .required)
            .foreignKey("grupaa_id", references: Grupaa.schema, .id, onDelete: .cascade, onUpdate: .noAction)
            .create()
        
    }

    func revert(on database: Database) -> EventLoopFuture<Void> {
        return database.schema("muzyk").delete()
    }
}