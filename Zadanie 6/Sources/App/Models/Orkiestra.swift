import Fluent
import Vapor

final class Orkiestra: Model, Content {
    static let schema = "orkiestra"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "nazwa")
    var nazwa: String
    
	@Field(key: "opis")
    var opis: String
	
	@Field(key: "np")
    var np: Int
    
    init() { }

    init(id: UUID? = nil, nazwa: String, opis: String, np: Int) {
        self.id = id
        self.nazwa = nazwa
		self.opis = opis
		self.np = np
    }
}