from src.models import Apartment
from src.manager import Manager
from src.models import Parameters
from src.models import Tenant

def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key
def test_tenants_loaded_properly():
    parameters = Parameters()
    manager = Manager(parameters)

    expected_names = [
        "Jan Nowak",
        "Adam Kowalski",
        "Ewa Adamska"
    ]

    for tenant_key, tenant in manager.tenants.items():
        assert tenant.name in expected_names, f"Nieoczekiwany najemca: {tenant.name}"

def test_tenants_apartments_assignment():
    parameters = Parameters()
    manager = Manager(parameters)
    
    assert manager.validate_tenants_apartments() is True, "Wszyscy najemcy powinni mieć przypisane istniejące mieszkania"
    
    first_tenant_key = list(manager.tenants.keys())[0]
    manager.tenants[first_tenant_key].apartment = "nieistniejace-mieszkanie"
    
    assert manager.validate_tenants_apartments() is False, "Metoda powinna wykryć przypisanie do nieistniejącego mieszkania"
