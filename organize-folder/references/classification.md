# Document Classification Rules

## PDF Metadata Extraction

When analyzing PDFs, search for the following keywords to categorize and extract details for renaming.

### Invoices

- **Keywords**: "Invoice", "Tax Invoice", "Bill To", "Invoice Number", "INV-", "Due Date".
- **Naming Format**: `yyyy-mm-dd-[VendorName]-[Invoice#]-[Amount].pdf`
- **Folder**: `Invoices/`

### Bills (Utility/Recurring)

- **Keywords**: "Statement of Account", "Service Period", "Account Number", "Utility Bill", "Electric", "Water", "Internet".
- **Naming Format**: `yyyy-mm-dd-[Provider]-[ServiceType].pdf`
- **Folder**: `Bills/`

### Receipts

- **Keywords**: "Receipt", "Transaction Date", "Order Summary", "Total Paid", "Store #", "Card Ending In".
- **Naming Format**: `yyyy-mm-dd-[Store]-[TotalAmount].pdf`
- **Folder**: `Receipts/`

### Travel Documents

- **Keywords**: "Itinerary", "Flight", "Boarding Pass", "Confirmation Number", "Booking Reference", "Airline", "Hotel Reservation".
- **Folder**: `Travel/`

### Financial/Legal

- **Bank Statements**: "Bank Statement", "Available Balance", "Checking Account".
- **Legal**: "Agreement", "Contract", "Terms and Conditions", "Privacy Policy".

## General File Types

### Photos & Media

- **Photos**: `.jpg`, `.jpeg`, `.png`, `.heic`, `.webp`. Move to `Photos/`.
- **Screenshots**: Filenames containing "Screenshot" (Windows/iOS) or "Screen Shot" (macOS). Move to `Photos/Screenshots/`.
- **Videos**: `.mp4`, `.mov`, `.mkv`, `.avi`. Move to `Videos/`.

### Installers

- **Extensions**: `.dmg`, `.pkg`, `.exe`, `.msi`, `.app` (if in a folder).
- **Folder**: `Installers/`

### Archives

- **Extensions**: `.zip`, `.tar.gz`, `.rar`, `.7z`.
- **Folder**: `Archives/`
