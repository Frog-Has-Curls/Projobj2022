import Fluent

struct CreateOrkiestra: Migration {
    func prepare(on database: Database) -> EventLoopFuture<Void> {
        return database.schema("orkiestra")
            .id()
            .field("nazwa", .string, .required)
            .field("opis", .string, .required)
            .field("np", .int, .required)
            .create()
    }

    func revert(on database: Database) -> EventLoopFuture<Void> {
        return database.schema("orkiestra").delete()
    }
}