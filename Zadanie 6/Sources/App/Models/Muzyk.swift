import Fluent
import Vapor

final class Muzyk: Model, Content {
    static let schema = "muzyk"
    
    @ID(key: .id)
    var id: UUID?

    @Field(key: "instrument")
    var instrument: String

    @Field(key: "opis")
    var opis: String
    
    @Field(key: "liczba")
    var liczba:  Int
    
    @Parent(key: "grupaa_id")
    var grupaa_id: Grupaa
    
    init() { }

    init(id: UUID? = nil, instrument: String, opis: String, liczba: Int) {
        self.id = id
        self.instrument = instrument
        self.opis = opis
        self.liczba = liczba
    }
}